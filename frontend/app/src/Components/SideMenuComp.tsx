import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import MenuListItem from "./MenuListItemComp";
import { menu } from '../Utils/layout';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import { Collapse } from '@mui/material';
import { useEffect, useState } from 'react';
import CollapseComp from './CollapseComp';


const drawerWidth = 300;
interface SideMenuProps {
  filters: string[],
  selectColumns: string[],
  setSelectColumns: React.Dispatch<React.SetStateAction<string[]>>,
  setSelectedFilter: React.Dispatch<React.SetStateAction<string>>;
}

const SideMenuComp: React.VFC<SideMenuProps> = ({ filters, setSelectedFilter, setSelectColumns, selectColumns }) => {
  const [open, setOpen] = React.useState(true);
  const handleClick = () => {
    setOpen(!open);
  };

  return (
  
    <Drawer
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: drawerWidth,
          border: 0,
          boxSizing: 'border-box',
        },
      }}
      variant="permanent"
      anchor="left"
    >
      <Toolbar />

      {menu.map((group) => {
        
        return (
          
          <CollapseComp filter={group.title} items={group.items} selectColumns={selectColumns} setSelectedFilter={setSelectedFilter} setSelectColumns={setSelectColumns} />
        );
        })
      }
    
      {filters.map((filter) => {
        return (
          <MenuListItem filter={filter} selectColumns={selectColumns} setSelectedFilter={setSelectedFilter} setSelectColumns={setSelectColumns} />
        );
        })
      }

    </Drawer>
    

  );
}
export default SideMenuComp