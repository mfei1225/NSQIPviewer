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

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import axios from "../Utils/axios";


const drawerWidth = 330;

interface DetailFilterMeta {
  searchTerm: number,
  filter: string,
  label: string
}
interface AddedFilterProps {
  filters: DetailFilterMeta[]
  setCount: React.Dispatch<React.SetStateAction<number>>

}
const AddedFilterComp: React.VFC<AddedFilterProps> = ({ filters, setCount}) => {


  const applyFilters = () => {
    console.log('hello')
    axios.post('filter', {
      filters:filters  
    }
    ).then((res) =>{
      setCount(res.data)
    }
    )
  }
return (

  <Drawer
    sx={{
      width: drawerWidth,
      flexShrink: 0,
      '& .MuiDrawer-paper': {
        width: drawerWidth,
        border: 0,
        boxSizing: 'border-box',
        m: 2
      },
    }}
    variant="permanent"
    anchor="right"
  >
    <Toolbar />
    <Box sx={{ m: 3 }}>
      {filters.map((filter) => {
        return (<Card sx={{ minWidth: 275 }} variant="outlined">
          <CardContent>
            <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
              {filter.filter}
            </Typography>
            <Typography variant="h5" component="div">
              {filter.label}
            </Typography>
            <Typography sx={{ mb: 1.5 }} color="text.secondary">
              {filter.searchTerm}
            </Typography>
          </CardContent>
          <CardActions>
            <Button size="small">Learn More</Button>
          </CardActions>
        </Card>

        );
      })
      }
    </Box>

    <Button variant="outlined" onClick={applyFilters}>apply filter</Button>

  </Drawer>

);
}
export default AddedFilterComp