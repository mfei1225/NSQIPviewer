import React from 'react';

import HomePage from './Pages/HomePage';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom';

function App() {
  return (
    //<DndProvider backend={HTML5Backend}>
  //<HomePage/>
 //</DndProvider>
 <Router>
        <Routes>
          <Route path="/" element={ <HomePage/>}/>
        </Routes>
      </Router>

  )
}

export default App;
