import React from "react";

const child = (x) => {
  console.log(x.users)
  let data=x.users //used for mapping
  return (
    // <>
    //   {/* <h3>
    //     My name is {e.data[0].name}.<br/> I am {e.data[0].age} old.<br/> Currently i am
    //     recideing in {e.data[0].city} <br/> i am {e.data[0].job}
    //   </h3>
    //   <h3>
    //     My name is {e.data[1].name}. I am {e.data[1].age} old. Currently i am
    //     recideing in {e.data[1].city} and i am in {e.data[1].job}
    //   </h3> */}

    // </>
    // --------------------------------------
    // <>
    //   <h1>{x.users[0].name}</h1>
    //   <h1>{x.users[0].age}</h1>
    //   <h1>{x.users[0].city}</h1>
    //   <h1>{x.users[0].country}</h1>
    //   <hr />
    //   <h1>{x.users[1].name}</h1>
    //   <h1>{x.users[1].age}</h1>
    //   <h1>{x.users[1].city}</h1>
    //   <h1>{x.users[1].country}</h1>
    //   <hr />
    // </>
    // ------------------------
    <>
    <div>
      <table border="2">
        <tr>
          <th>name</th>
          <th>age</th>
          <th>city</th>
          <th>country</th>
        </tr>
        {/* <tr>
          <td>{x.users[0].name}</td>
          <td>{x.users[0].age}</td>
          <td>{x.users[0].city}</td>
          <td>{x.users[0].country}</td>
        </tr> */}
        {
          data.map((info)=>{
            return(
              <tr>
                <td>{info.name}</td>
                <td>{info.age}</td>
                <td>{info.city}</td>
                <td>{info.country}</td>
              </tr>
            )
          })
        }
      </table>
    </div>
    </>
  );
};

export default child;
