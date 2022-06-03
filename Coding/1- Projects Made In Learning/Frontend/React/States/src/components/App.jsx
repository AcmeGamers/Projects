import React, { useState } from "react";

export default function App() {
  const [properties, setProperties] = useState({
    fName: "",
    lName: "",
    email: "",
  });
  function updateProperties(e) {
    setProperties({
      ...properties,
      [e.target.name]: e.target.value,
    });
  }
  return (
    <div className="container">
      <form>
        <h1>
          Hello, {properties.fName} {properties.lName}, Email:{" "}
          {properties.email}
        </h1>
        <input
          name="fName"
          onChange={updateProperties}
          placeholder="First Name"
        />
        <input
          type="text"
          name="lName"
          onChange={updateProperties}
          placeholder="Last Name"
        />
        <input
          type="email"
          name="email"
          onChange={updateProperties}
          placeholder="Email"
        />
        <button>Click Me</button>
      </form>
    </div>
  );
}
