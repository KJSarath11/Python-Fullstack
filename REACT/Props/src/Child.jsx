import React from 'react'

export const Child = (x) => {
  return (
    <>
    <div>My name is {x.data[0]}</div>
    <div>My friend is {x.data[1]}</div>
    <div>I love {x.data[2]}</div>
    </>
  )
}
export default Child
a