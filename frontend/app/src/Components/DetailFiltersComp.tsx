import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import { useEffect, useState } from 'react';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ChipComp from "./MenuListItemComp";
import axios from "../Utils/axios";
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';


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
    const DetailFilterDefualt = {
        searchTerms: [],
        filter: "",
        label: "",
    };
    const [firstRender, setFirstRender] = useState(true);
    const [label, setLabel] = useState("Select Filter")
    const [searchTerm, setSearchTerm] = useState<number>(0)
    const [allSearchTerm, setAllSearchTerm] = useState<number[]>([])
    const [filterType, setFilterType] = useState<string>("")

    useEffect(() => {

        if (firstRender) setFirstRender(false);
        if (!firstRender) {
            axios.get('columns/details/' + filter)
                .then((res) => {
                    setLabel(res.data['label'])
                    setFilterType(res.data['type'])
                })
        }
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

    const handleChange = (event: any) => {
        setSearchTerm(event.target.value)
    };

    return (
        <div>
            <Toolbar />
            <Box
                component="main"
                sx={{ bgcolor: 'background.default', p: 3, width: 300 }}
            >{label}

                {filterType == 'IntegerField' ? <TextField
                    label="Search"
                    variant="outlined"
                    onChange={handleChange}
                    name="Search"
                /> : ''
                }
                Added filters:
                {
                allSearchTerm.map((item) => {
                    return(
                        <div>
                            {item}
                        </div>
                    )
                })
                    }
                <Button variant="outlined" onClick={addToFilter}>Add Filter(OR logic)</Button>
                <Button variant="outlined" onClick={addToFunnel}>Add to Funnel</Button>
            </Box>
        </div>
    );
}
export default DetailFiltersComp