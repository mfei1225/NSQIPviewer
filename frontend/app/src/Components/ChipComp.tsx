import React from 'react'
import Chip from "@mui/material/Chip";
import { useDrag } from 'react-dnd';

function ChipComp({ name }: { name: string }) {
  const [{ isDragging }, drag] = useDrag(() => ({
    type: "Chip",
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));
  return (
  
    <Chip
                  //icon={icon}
                  variant="outlined"
                  sx={{ m: 0.5 }}
                  label={name}
                  ref={drag}
                  //onDelete={data.label === 'React' ? undefined : handleDelete(data)}
                />
               
  )
}

export default ChipComp