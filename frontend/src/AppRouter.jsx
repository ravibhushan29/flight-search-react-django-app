import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './Login/Login';
import FlightSearch from './FlightSearch/FlightSearch';

const AppRouter = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/flight-search" element={<FlightSearch />} />
      </Routes>
    </Router>
  );
};

export default AppRouter;
