// import React, { useState } from "react";

// const App = () => {
//   let [name, setname] = useState();
//   let [age, setage] = useState();
//   let [city, setcity] = useState();
//   let [data, setdata] = useState();

//   let handleForm = (e) => {
//     e.preventDefault();
//     let list = { name, age, city };
//     setdata(list);
//   };

//   return (
//     <div>
//       <form onSubmit={handleForm}>
//         <label htmlFor="">Name:</label>
//         <input
//           type="text"
//           value={name}
//           onChange={(e) => {
//             setname(e.target.value);
//           }}
//         />
//         <label htmlFor="">Age:</label>
//         <input
//           type="text"
//           value={age}
//           onChange={(e) => {
//             setage(e.target.value);
//           }}
//         />
//         <label htmlFor="">City:</label>
//         <input
//           type="text"
//           value={city}
//           onChange={(e) => {
//             setcity(e.target.value);
//           }}
//         />
//         <button type="submit">Submit</button>
//       </form>
//       {data && (
//         <table border="2">
//           <tr>
//             <th>Name</th>
//             <th>Age</th>
//             <th>City</th>
//           </tr>
//           <tr>
//             <td>{data.name}</td>
//             <td>{data.age}</td>
//             <td>{data.city}</td>
//           </tr>
//         </table>
//       )}
//     </div>
//   );
// };

// export default App;
