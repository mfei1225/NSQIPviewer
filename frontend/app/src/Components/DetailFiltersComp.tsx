import * as React from 'react';
import Box from '@mui/material/Box';

import Toolbar from '@mui/material/Toolbar';
import { useEffect, useState } from 'react';

import axios from "../Utils/axios";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';


const drawerWidth = 230;

interface DetailFilterMeta {
    searchTerms: number[],
    filter: string,
    label: string
}
interface DetailFiltersProps {
    filter: string,
    addedFilters: DetailFilterMeta[],
    setAddedFilters: React.Dispatch<React.SetStateAction<DetailFilterMeta[]>>
}

const DetailFiltersComp: React.VFC<DetailFiltersProps> = ({ filter, addedFilters, setAddedFilters }) => {

    const [firstRender, setFirstRender] = useState(true);
    const [label, setLabel] = useState("Select Filter")
    const [searchTerm, setSearchTerm] = useState<number>(0)
    const [allSearchTerm, setAllSearchTerm] = useState<any[]>([])
    const [filterType, setFilterType] = useState<string>("")
    const [filterValues, setFilterValues] = useState<string[]>([])

    useEffect(() => {

        if (firstRender) setFirstRender(false);
        if (!firstRender) {
            axios.get('columns/details/' + filter.split(' ').join("_"))
                .then((res) => {
                    setLabel(res.data['label'])
                    setFilterType(res.data['type'])
                    setFilterValues(res.data['values'])
                })
        }
        setAllSearchTerm([])
    }, [filter])

    const addToFilter = () => {
        setAllSearchTerm([
            ...allSearchTerm, searchTerm
        ]);
    }



    const addToFunnel = () => {
        setAddedFilters([...addedFilters,
        {
            'searchTerms': allSearchTerm,
            'filter': filter,
            'label': label
        }]);
        setAllSearchTerm([])

    }

    const handleChangeTextbox = (event: any) => {
        setSearchTerm(event.target.value)
    };
    const handleChangeCheckbox = (event: any, selected_item: any) => {
        if (event.target.checked) {
            setAllSearchTerm([...allSearchTerm, selected_item])
        }
        else {
            setAllSearchTerm((allSearchTerm) =>
                allSearchTerm.filter((item) => item !== selected_item)
            );
        }
    };


    return (
        <div>
            <Toolbar />
            <Box
                component="main"
                sx={{ bgcolor: 'background.default', p: 3, width: 300 }}
            >{label}

                {
                    filterValues.length == 0 ? <div> <TextField
                        label="Search"
                        variant="outlined"
                        onChange={handleChangeTextbox}
                        name="Search"
                    />
                        Added filters:
                        {
                            allSearchTerm.map((item) => {
                                return (
                                    <div>
                                        {item}
                                    </div>
                                )
                            })
                        }
                        <Button variant="outlined" onClick={addToFilter}>Add Filter(OR logic)</Button>
                    </div>
                        : <FormGroup>
                            {
                                filterValues.sort().map((item) => {
                                    if (item != "NULL") {
                                        return (
                                            <FormControlLabel control={<Checkbox onChange={event => handleChangeCheckbox(event, item)} />} label={item} />
                                        )
                                    }
                                })
                                
                                  
                            }
                            {filterValues.includes("NULL")&&<FormControlLabel control={<Checkbox onChange={event => handleChangeCheckbox(event, 'NULL')} />} label="NULL" />}
                            
                        </FormGroup>
                }

                <Button variant="outlined" onClick={addToFunnel}>Add to Funnel</Button>
            </Box>
        </div>
    );
}
export default DetailFiltersComp