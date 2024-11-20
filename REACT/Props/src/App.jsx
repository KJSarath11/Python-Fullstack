// import React, { Component } from 'react'
import React, { useState } from "react";

const App = () => {
  const [name, setname] = useState();
  const [number, setnumber] = useState();
  const [city, setcity] = useState();
  const [country, setcountry] = useState();
  const [data, setdata] = useState();

  const handleSubmit = (e) => {
    e.preventDefault();
    const list = { name, number, city, country };
    setdata(list);
  };
  return (
    <div>
      /* Forms using States */
      <form onSubmit={handleSubmit}>
        <label htmlFor="">Enter Your Name: </label>
        {
          <input
            type="text"
            value={name}
            onChange={(e) => {
              setname(e.target.value);
            }}
          />
        }
        <br />
        <br />
        <br />

        <label htmlFor="">Enter Your Number: </label>
        <input
          type="text"
          value={number}
          onChange={(e) => {
            setnumber(e.target.value);
          }}
        />
        <br />
        <br />
        <br />

        <label htmlFor="">Enter Your City: </label>
        <input
          type="text"
          value={city}
          onChange={(e) => {
            setcity(e.target.value);
          }}
        />
        <br />
        <br />
        <br />

        <label htmlFor="">Enter the Country: </label>
        {
          <input
            type="text"
            value={country}
            onChange={(e) => {
              setcountry(e.target.value);
            }}
          />
        }
        <br />
        <br />
        <br />

        <input type="submit" value="Submit" />
        <br />
        <br />
        <br />
      </form>
      {/* <h1>{name}</h1>
      <h1>{number}</h1>
      <h1>{city}</h1> */}
      {data && (
        <table border="1">
          <tr>
            <th>Name</th>
            <th>Number</th>
            <th>City</th>
            <th>Country</th>
          </tr>

          <tr>
            <td>{data.name}</td>
            <td>{data.number}</td>
            <td>{data.city}</td>
            <td>{data.country}</td>
          </tr>
        </table>
      )}
    </div>
  );
};

export default App;
