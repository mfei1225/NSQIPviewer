import React from "react";
import {useEffect, useState} from 'react';
import ChipComp from "../Components/MenuListItemComp";
import Box from '@mui/material/Box';
import SideMenuComp from "../Components/SideMenuComp";
import DetailFiltersComp from "../Components/DetailFiltersComp";
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Typography from '@mui/material/Typography';
import Toolbar from '@mui/material/Toolbar';

import axios from "../Utils/axios";
const drawerWidth = 240;

const HomePage: React.VFC = () => {
    const [count, setCount] = useState(0)
    const [columns, setColumns] = useState([])
    const [selectedFilter, setSelectedFilter] = useState("Select Filter")

    useEffect(() =>{
        const getCount = async() =>{
            try{
                const response = await axios.get('api/record/count');
                setCount(response.data)
            } catch (err){
                
            }
        }
        getCount()
    },[])

    useEffect(() =>{
        const getColumns = async() =>{
            try{
                const response = await axios.get('api/columns');
                setColumns(response.data)
            } catch (err){
                
            }
        }
        getColumns()
    },[])

    return (
        
    
            <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar
        position="fixed"
        sx={{ width: `calc(100% - ${drawerWidth}px)`, ml: `${drawerWidth}px` }}
      >
 
      </AppBar>
      <SideMenuComp filters={columns} setSelectedFilter={setSelectedFilter}/>
      <DetailFiltersComp filter={selectedFilter}/>
      
    
       
           
       
            {count}
            
           
         </Box>

  

    );
};

export default HomePage;


    //const [columns, setColumns] = useState([])
/** 
    useEffect(() =>{
        const getCount = async() =>{
            try{
                const response = await axios.get('api/record/count');
                setCount(response.data)
            } catch (err){
                
            }
        }
        getCount()
    },[])

    useEffect(() =>{
        const getColumns = async() =>{
            try{
                const response = await axios.get('api/columns');
                setColumns(response.data)
            } catch (err){
                
            }
        }
        getColumns()
    },[])
*/