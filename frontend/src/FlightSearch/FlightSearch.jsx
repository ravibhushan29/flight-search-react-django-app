import React, { useState } from 'react';
import FlightResults from './FlightResults';
import './FlightSearch.css'

// Mock flight data based on the provided JSON sample
const mockFlights = [
  // Include a few examples from your JSON data
  {
    "id": 1,
    "flight": { "flight_number": "wuv523", "airline_name": "Iberia" },
    "source_city": "New York",
    "destination_city": "Los Angeles",
    "departure_time": "2024-03-02T18:27:11.348581Z",
    "arrival_time": "2024-03-02T19:27:11.348581Z",
    "duration": "01:00:00",
    "no_of_stops": 1,
    "price": "433.53"
  },
  {
    "id": 2,
    "flight": { "flight_number": "wuv523", "airline_name": "Iberia" },
    "source_city": "Chicago",
    "destination_city": "Houston",
    "departure_time": "2024-03-04T00:51:11.356381Z",
    "arrival_time": "2024-03-04T02:51:11.356381Z",
    "duration": "02:00:00",
    "no_of_stops": 1,
    "price": "347.24"
  },
  // Add more flights as needed...
];

const FlightSearch = () => {
  const cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"];

  const [searchParams, setSearchParams] = useState({
    departureCity: '',
    destinationCity: '',
    departureDate: '',
  });
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSearchParams(prevState => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
  e.preventDefault();
  setLoading(true);

  // Construct the API URL with query parameters
  const apiUrl = `http://127.0.0.1:8000/api/v1/flight-journey/?source_city=${encodeURIComponent(searchParams.departureCity)}&destination_city=${encodeURIComponent(searchParams.destinationCity)}&travel_date=${encodeURIComponent(searchParams.departureDate)}`;

  try {
    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    setSearchResults(data); // Assume the API returns an array of flight objects
  } catch (error) {
    console.error("Failed to fetch flight data:", error);
    // Optionally, set an error state here to notify the user
  } finally {
    setLoading(false);
  }
};


  return (
    <div>
      <form className='search-form' onSubmit={handleSubmit}>
        <label>
          <span>Departure City:</span>
          <select name="departureCity" value={searchParams.departureCity} onChange={handleInputChange} required>
            <option value="">Select a city</option>
            {cities.map(city => (
              <option key={city} value={city}>{city}</option>
            ))}
          </select>
        </label>

        <label>
          <span>Destination City:</span>
          <select name="destinationCity" value={searchParams.destinationCity} onChange={handleInputChange} required>
            <option value="">Select a city</option>
            {cities.map(city => (
              <option key={city} value={city}>{city}</option>
            ))}
          </select>
        </label>

        <label>
          <span>Departure Date:</span>
          <input
            type="date"
            name="departureDate"
            value={searchParams.departureDate}
            onChange={handleInputChange}
            required
          />
        </label>

        <button className='btn-search' type="submit" disabled={loading}>
          {loading ? 'Searching...' : 'Search Flights'}
        </button>
      </form>

      {!loading && searchResults.length > 0 && (
        <div>
          <h2>Flight Results : {searchResults.length}</h2>
          <FlightResults results={searchResults}/>
        </div>
      )}
    </div>
  );
};

export default FlightSearch;
