import React from 'react';
import './FlightResults.css'; // Make sure this path matches your CSS file location

const FlightResults = ({ results }) => {
  if (results.length === 0) {
    return (
      <div className="flight-results-container">
        <h2>No flights found</h2>
        <p>Please try a different search.</p>
      </div>
    );
  }

  return (
    <div className="flight-results-container">
      <ul>
        {results.map(flight => (
          <li key={flight.id} className="flight-item">
            <div>
              <h3>Flight: {flight.flight.flight_number} ({flight.flight.airline_name})</h3>
              <strong>From:</strong> {flight.source_city} &nbsp; &nbsp; <strong>To:</strong> {flight.destination_city}
            </div>

            <div>
              <strong>Departure:</strong> {new Date(flight.departure_time).toLocaleString()} &nbsp; &nbsp;
              <strong>Arrival:</strong> {new Date(flight.arrival_time).toLocaleString()}
            </div>

            <div>
              <strong>Duration:</strong> {flight.duration} &nbsp; &nbsp;
              <strong>Stops:</strong> {flight.no_of_stops} stop(s)
            </div>

            <div>
              <strong>Price:</strong> ${flight.price}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FlightResults;
