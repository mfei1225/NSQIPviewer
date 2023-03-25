import React from 'react'
import Chip from "@mui/material/Chip";

import MoreVertIcon from '@mui/icons-material/MoreVert';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import axios from "../Utils/axios";

interface MenuListProps {
  filter:string,
  setSelectedFilter:React.Dispatch<React.SetStateAction<string>>;
}
const MenuListItemComp: React.VFC<MenuListProps>=({filter,setSelectedFilter}) =>{
  const getLabel = () =>{
    const getLabelhelper = async() =>{
      console.log(filter)
      try{
          const response = await axios.get('api/columns/single/'+filter);
          setSelectedFilter(response.data)
      } catch (err){
        console.log(err)
          
      }
  }
  getLabelhelper()
      
  }
  return (
  <div>
     <ListItem key={filter} disablePadding>
              <ListItemButton onClick={getLabel}>
                <ListItemText primary={filter} />
              </ListItemButton>
        </ListItem>
    </div>     
  )
}

export default MenuListItemComp