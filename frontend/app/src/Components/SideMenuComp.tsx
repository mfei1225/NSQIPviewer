import * as React from 'react';

import Drawer from '@mui/material/Drawer';

import Toolbar from '@mui/material/Toolbar';

import MenuListItem from "./MenuListItemComp";
import { menu } from '../Utils/layout';

import CollapseComp from './CollapseComp';
import TextField from '@mui/material/TextField';
import { useEffect, useState } from 'react';

const drawerWidth = 300;
interface SideMenuProps {
  filters: string[],
  selectColumns: string[],
  setSelectColumns: React.Dispatch<React.SetStateAction<string[]>>,
  setSelectedFilter: React.Dispatch<React.SetStateAction<string>>;

}

const SideMenuComp: React.VFC<SideMenuProps> = ({ filters,setSelectedFilter, setSelectColumns, selectColumns }) => {

  const [searchTerm, setSearchTerm] = useState<any>("")
  const [filteredFilters, setFilteredFilters] = useState<string[]>([])
  const handleChangeTextbox = (event: any) => {
    setSearchTerm(event.target.value)
    setFilteredFilters((filteredFilters) =>
    filters.filter((item) =>  item.includes(event.target.value))
  );
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
      <TextField
                        label="Search"
                        variant="outlined"
                        onChange={handleChangeTextbox}
                        name="Search"
                    />
      {!searchTerm?menu.map((group) => {
        
        return (
          
          <CollapseComp filter={group.title} items={group.items} selectColumns={selectColumns} setSelectedFilter={setSelectedFilter} setSelectColumns={setSelectColumns} />
        );
        }):
        filteredFilters.sort(function(a, b){
          return  a.length-b.length;
        }).map((filter) => {
          return (
            <MenuListItem filter={filter} selectColumns={selectColumns} setSelectedFilter={setSelectedFilter} setSelectColumns={setSelectColumns} />
          );
          })
        
      }
    
      

    </Drawer>
    

  );
}
export default SideMenuComp