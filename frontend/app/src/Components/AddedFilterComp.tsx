import * as React from 'react';
import { useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';

import Toolbar from '@mui/material/Toolbar';

import Typography from '@mui/material/Typography';

import { Link } from "react-router-dom";
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import axios from "../Utils/axios";
import CircularProgress from '@mui/material/CircularProgress';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';



const drawerWidth = 240;

interface dbCount {
  db: string,
  count: number,
}

interface DetailFilterMeta {
  searchTerms: number[],
  filter: string,
  label: string
}
interface AddedFilterProps {
  filters: DetailFilterMeta[],
  selectColumns: string[],
  setIsLoadingCount: React.Dispatch<React.SetStateAction<boolean>>,
  setCount: React.Dispatch<React.SetStateAction<dbCount[]>>
  setAddedFilters: React.Dispatch<React.SetStateAction<DetailFilterMeta[]>>
}
const AddedFilterComp: React.VFC<AddedFilterProps> = ({ filters, setIsLoadingCount, selectColumns, setCount, setAddedFilters }) => {
  const [isLoadingExport, setIsLoadingExport] = useState(false)
  const [excludeNull, setExcludeNull] = useState(true)
  const applyFilters = () => {

    setIsLoadingCount(true)
    axios.post('filter', {
      filters: filters,
      selectColumns: selectColumns
    }
    ).then((res) => {
      const dbcount:dbCount[] = []
      var keys:any= new Set()
      console.log(res.data)
      Object.keys(res.data).forEach(function(key, index) {
        console.log(...Object.keys(res.data[key][0]))
        keys.add(...Object.keys(res.data[key][0]))
      })
      
      keys = Array.from(keys);
      console.log(keys)
      var replacer = function(key:any, value:any) { 
        if(value === null ||value === undefined ){
          return 'NULL'
        }
        return value
      }
      Object.keys(res.data).forEach(function(key, index) {
  
        var csv = res.data[key].map(function(row:any){
          var array = keys.map(function(fieldName:any){
            return JSON.stringify(row[fieldName], replacer)
          })
          if(excludeNull){
            if (array.includes("\"NULL\"") || array.includes("-99")){
              return 
            }
          }
        
          return array.join(',')
        })
    
        csv = csv.filter(function( element:any ) {
          return element !== undefined;
       });

       
        dbcount.push(
          {'db':key,'count':csv.length}
        )
      });
     
      setCount(dbcount)
      setIsLoadingCount(false)
    }
    )
  }

  const deleteFilter = (filter: DetailFilterMeta) => {

    setAddedFilters((filters) =>
      filters.filter((item) => item !== filter)
    );
  }

  const handleChangeCheckbox = (event: any) => {
    if (event.target.checked) {
      setExcludeNull(true)
    }
    else {
      setExcludeNull(false)
    }
  };


  const applyFiltersAndExport = () => {
    setIsLoadingExport(true)

    axios.post('filter/export', {
      filters: filters,
      selectColumns: selectColumns
    }
    ).then((res) => {
      const keys:any= Object.keys(res.data[0])
  
      var replacer = function(key:any, value:any) { 
        if(value === null ||value === undefined ){
          return 'NULL'
        }
        return value
      }

     
      var csv = res.data.map(function(row:any){
        const array = keys.map(function(fieldName:any){
          return JSON.stringify(row[fieldName], replacer)
        })
        if(excludeNull){
          if (array.includes("\"NULL\"") ||array.includes("-99")){
            return 
          }
        }
        return array.join(',')
      })
      csv = csv.filter(function( element:any ) {
        return element !== undefined;
     });
      csv.unshift(keys.join(',')) // add header column
      csv = csv.join('\r\n');
    
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const pom = document.createElement('a');
      pom.href = url;
      pom.setAttribute('download', "Data.csv");
      pom.click();
      setIsLoadingExport(false)
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
      <FormGroup>
        <FormControlLabel control={<Checkbox defaultChecked onChange={handleChangeCheckbox} />} label="Exclude Null Values" />
      </FormGroup>
      <Box sx={{ m: 3 }}>
        {filters.map((filter) => {
          return (<Card sx={{ minWidth: 210 }} variant="outlined">
            <CardContent>
              <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                {filter.filter}
              </Typography>
              <Typography variant="h5" component="div">
                {filter.label}
              </Typography>
              <Typography sx={{ mb: 1.5 }} color="text.secondary">
                {filter.searchTerms.join(',')}
              </Typography>
            </CardContent>
            <CardActions>
              <Button size="small" onClick={() => deleteFilter(filter)}>Delete</Button>
            </CardActions>
          </Card>

          );
        })
        }

      </Box>


      <Button variant="outlined" onClick={applyFilters}>Apply Funnel Filter</Button>

      {isLoadingExport ? <CircularProgress /> : <Button variant="outlined" onClick={applyFiltersAndExport}>Apply Funnel Filter and export</Button>}

      <Link to="/Data"><Button variant="outlined" onClick={applyFilters}>Look At Data</Button></Link>


    </Drawer>

  );
}
export default AddedFilterComp