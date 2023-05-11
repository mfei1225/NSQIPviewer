import React from 'react';

import HomePage from './Pages/HomePage';
import DataPage from './Pages/DataPage';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';

function App() {
  return (

 <Router>
        <Routes>
          <Route path="/" element={ <HomePage/>}/>
          <Route path="/data" element={ <DataPage/>}/>
        </Routes>
      </Router>

  )
}

export default App;
