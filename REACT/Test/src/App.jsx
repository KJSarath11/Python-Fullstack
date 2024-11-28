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

//? Controlled forms
// import React, { useRef, useState } from "react";

// const App = () => {
//   let n1 = useRef();
//   let n2 = useRef();
//   let [res, setres] = useState();

//   let add = (e) => {
//     e.preventDefault();
//     let a = n1.current.value;
//     let b = n2.current.value;
//     setres(parseInt(a) + parseInt(b));
//   };
//   let sub = (e) => {
//     e.preventDefault();
//     let a = n1.current.value;
//     let b = n2.current.value;
//     setres(a - b);
//   };
//   let mul = (e) => {
//     e.preventDefault();
//     let a = n1.current.value;
//     let b = n2.current.value;
//     setres(a * b);
//   };
//   let div = (e) => {
//     e.preventDefault();
//     let a = n1.current.value;
//     let b = n2.current.value;
//     setres(a / b);
//   };
//   return (
//     <div>
//       <h1>Controlled Forms: </h1>;
//       <form action="">
//         <label htmlFor="">N1:</label>
//         <input type="number" ref={n1} />
//         <br />
//         <br />
//         <label htmlFor="">N2:</label>
//         <input type="number" ref={n2} />
//         <br />
//         <br />
//         <button type="submit" onClick={add}>
//           ADD
//         </button>
//         <button type="submit" onClick={sub}>
//           SUB
//         </button>
//         <button type="submit" onClick={mul}>
//           MUL
//         </button>
//         <button type="submit" onClick={div}>
//           DIV
//         </button>
//       </form>
//       <h1>Result is :{res}</h1>
//     </div>
//   );
// };

// export default App;

// Uncontrolled Forms
import React, { useState } from "react";

const App = () => {
  let [n1, setn1] = useState();
  let [n2, setn2] = useState();
  let [res, setres] = useState();

  let n1data = (e) => {
    setn1(e.target.value);
  };
  let n2data = (e) => {
    setn2(e.target.value);
  };

  let add = (e) => {
    e.preventDefault();
    let a = n1;
    let b = n2;
    setres(parseInt(a) + parseInt(b));
  };
  let sub = (e) => {
    e.preventDefault();
    let a = n1;
    let b = n2;
    setres(parseInt(a) - parseInt(b));
  };
  let mul = (e) => {
    e.preventDefault();
    let a = n1;
    let b = n2;
    setres(parseInt(a) * parseInt(b));
  };
  let div = (e) => {
    e.preventDefault();
    let a = n1;
    let b = n2;
    setres(parseInt(a) / parseInt(b));
  };
  return (
    <div>
      <h1>Uncontrolled Forms: </h1>
      <form action="">
        <label htmlFor="">N1:</label>
        <input type="text" value={n1} onChange={n1data} />
        <br />
        <br />
        <label htmlFor="">N2:</label>
        <input type="text" value={n2} onChange={n2data} />
        <br />
        <br />
        <button onClick={add}>Add</button>
        &nbsp;
        <button onClick={sub}>SUB</button>
        &nbsp;
        <button onClick={mul}>MUL</button>
        &nbsp;
        <button onClick={div}>DIV</button>
        &nbsp;
      </form>
      <h1>Result is: {res}</h1>
    </div>
  );
};

export default App;
