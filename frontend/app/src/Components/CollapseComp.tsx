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
import Checkbox from '@mui/material/Checkbox';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import Collapse from '@mui/material/Collapse';
import MenuListItem from "./MenuListItemComp";


interface MenuListProps {
  filter: string,
  items:string[]
  selectColumns: string[],
  setSelectColumns: React.Dispatch<React.SetStateAction<string[]>>,
  setSelectedFilter: React.Dispatch<React.SetStateAction<string>>;
}
const CollapseComp: React.VFC<MenuListProps> = ({ filter,items,selectColumns,setSelectColumns,setSelectedFilter }) => {
    const [open, setOpen] = React.useState(false);

    const handleClick = () => {
        setOpen(!open);
    };

  
  const label = { inputProps: { 'aria-label': 'Checkbox demo' } };
  return (
    <div>
    <ListItemButton onClick={handleClick}>
    <ListItemText primary={filter}/>
    {open ? <ExpandLess /> : <ExpandMore />}
  </ListItemButton >
    
    <Collapse in={open} timeout="auto" unmountOnExit>
        {items.map((filter) => {
        return (
          <MenuListItem filter={filter} selectColumns={selectColumns} setSelectedFilter={setSelectedFilter} setSelectColumns={setSelectColumns} />
        );
        })
      }
      </Collapse>
    </div>
  )
}

export default CollapseComp

// {//onClick={getLabel} <Checkbox {...label} onChange={handleChange} />}