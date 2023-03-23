import React from "react";
import {useEffect, useState} from 'react';

import axios from "../Utils/axios";

const HomePage: React.VFC = () => {
    const [count, setCount] = useState(0)

    useEffect(() =>{
        const patientCount = async() =>{
            try{
                const response = await axios.get('api/record/count');
                setCount(response.data)
            } catch (err){
                
            }
        }
        patientCount()
    },[])

    return (
        <div>
            {count}
        </div>
    );
};

export default HomePage;