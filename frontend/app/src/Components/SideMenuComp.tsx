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


const drawerWidth = 230;
interface SideMenuProps {
  filters:string[]
  ,
  setSelectedFilter:React.Dispatch<React.SetStateAction<string>>;
}

const SideMenuComp: React.VFC<SideMenuProps>=({filters,setSelectedFilter}) =>{
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
   
        {filters.map((filter) => {
              return ( <MenuListItem filter={filter} setSelectedFilter={setSelectedFilter} />
              );
            })
            }
     
      </Drawer>
   
  );
}
export default SideMenuComp