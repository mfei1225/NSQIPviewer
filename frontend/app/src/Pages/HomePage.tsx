import React from "react";
import {useEffect, useState} from 'react';
import ChipComp from "../Components/ChipComp";
import Box from '@mui/material/Box';
import SideMenuComp from "../Components/SideMenuComp";
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Typography from '@mui/material/Typography';
import Toolbar from '@mui/material/Toolbar';

import axios from "../Utils/axios";
const drawerWidth = 240;

const HomePage: React.VFC = () => {
    const [count, setCount] = useState(0)
    const [columns, setColumns] = useState([])

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
      <SideMenuComp/>
      <Box
        component="main"
        sx={{ flexGrow: 1, bgcolor: 'background.default', p: 3 }}
      >
           
       
            {count}
            
            {columns.map((columns) => {
              return ( <ChipComp name={columns} />
              );
            })
            }
         </Box>
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