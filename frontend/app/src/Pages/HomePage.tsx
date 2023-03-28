import React from "react";
import { useEffect, useState } from 'react';
import ChipComp from "../Components/MenuListItemComp";
import Box from '@mui/material/Box';
import SideMenuComp from "../Components/SideMenuComp";
import DetailFiltersComp from "../Components/DetailFiltersComp";
import AddedFilterComp from "../Components/AddedFilterComp";
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Typography from '@mui/material/Typography';
import Toolbar from '@mui/material/Toolbar';
import CircularProgress from '@mui/material/CircularProgress';

import axios from "../Utils/axios";

const drawerWidth = 240;

interface DetailFilterMeta {
    searchTerms: number[],
    filter: string,
    label: string
}

interface dbCount {
    db: string,
    count: number,
}
const HomePage: React.VFC = () => {
    const [count, setCount] = useState<dbCount[]>([])
    const [columns, setColumns] = useState([])
    const [addedFilters, setAddedFilters] = useState<DetailFilterMeta[]>([])
    const [selectedFilter, setSelectedFilter] = useState("")
    const [selectColumns, setSelectColumns] = useState<string[]>([])
    const [isLoadingCount, setIsLoadingCount] = useState(true)

    useEffect(() => {
        const getCount = async () => {
            try {
                const response = await axios.get('record/count');
                setCount(response.data)
            } catch (err) {

            }
            setIsLoadingCount(false)
        }
        getCount()
    }, [])

    useEffect(() => {
        const getColumns = async () => {
            try {
                const response = await axios.get('columns');
                setColumns(response.data)
            } catch (err) {

            }
        }
        getColumns()
    }, [])

    return (


        <Box sx={{ display: 'flex' }}>
            <CssBaseline />
            <AppBar
                position="fixed"
                sx={{ width: `calc(100% - ${drawerWidth}px)`, ml: `${drawerWidth}px` }}
            >

            </AppBar>
            <SideMenuComp filters={columns} setSelectedFilter={setSelectedFilter} setSelectColumns={setSelectColumns} selectColumns={selectColumns}/>
            <DetailFiltersComp filter={selectedFilter} addedFilters={addedFilters} setAddedFilters={setAddedFilters} />
            <Box
                component="main"
                sx={{ bgcolor: 'background.default', p: 3, width: 300 }}
            >
            {isLoadingCount ? <CircularProgress /> :
                
                count.map((item) => {
                    return(
                        <div>
                            {item.db} : {item.count}
                        </div>
                    )
                })
            }
                <div>
                    
                    total : {Object.values(count).reduce((a, b) => a + b.count, 0)}
                </div>
            </Box>
            <AddedFilterComp filters={addedFilters} setCount={setCount} setIsLoadingCount={setIsLoadingCount} selectColumns={selectColumns} />




        </Box>



    );
};

export default HomePage;


