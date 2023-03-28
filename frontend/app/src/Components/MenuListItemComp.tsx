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


interface MenuListProps {
  filter: string,
  selectColumns: string[],
  setSelectedFilter: React.Dispatch<React.SetStateAction<string>>;
  setSelectColumns: React.Dispatch<React.SetStateAction<string[]>>,
}
const MenuListItemComp: React.VFC<MenuListProps> = ({ filter, setSelectedFilter, selectColumns, setSelectColumns }) => {
  const getLabel = () => {
    setSelectedFilter(filter)

  }

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.checked) {
      setSelectColumns([...selectColumns, filter])
    }
    else {
      setSelectColumns((selectColumns) =>
        selectColumns.filter((item) => item !== filter)
      );
    }
  };
  
  const label = { inputProps: { 'aria-label': 'Checkbox demo' } };
  return (
    
    <div>
      <ListItem key={filter} disablePadding>
        <ListItemButton onClick={getLabel} sx={{ pl: 4 }}>
          <ListItemText primary={filter} />
          <Checkbox {...label} onChange={handleChange} />
        </ListItemButton>
      </ListItem>
    </div>
  )
}

export default MenuListItemComp