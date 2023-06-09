import * as React from 'react';
import { useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';

import Toolbar from '@mui/material/Toolbar';

import Typography from '@mui/material/Typography';


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
  const [includeNull, setIncludeNull] = useState(false)
  const applyFilters = () => {

    setIsLoadingCount(true)
    axios.post('filter', {
      filters: filters
    }
    ).then((res) => {

      setCount(res.data)
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
      setIncludeNull(true)
    }
    else {
      setIncludeNull(false)
    }
  };


  const applyFiltersAndExport = () => {
    setIsLoadingExport(true)

    axios.post('filter/export', {
      filters: filters,
      selectColumns: selectColumns
    }
    ).then((res) => {

      const array = [Object.keys(res.data[0])].concat(res.data)
      const csv = array.map(it => {
        return Object.values(it).toString()
      }).join('\n')
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


    </Drawer>

  );
}
export default AddedFilterComp