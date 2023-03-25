import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import {useEffect, useState} from 'react';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import ChipComp from "./MenuListItemComp";


const drawerWidth = 230;

export default function DetailFiltersComp({ filter }: { filter: string }) {
  
  return (
    <div>
    <Toolbar />
    <Box
    component="main"
    sx={{  bgcolor: 'background.default', p: 3, width: 300 }}
  >{filter}
  
  </Box>
   </div>
  );
}
