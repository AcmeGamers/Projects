import React from "react";

export default function TodoList(props) {
  return (
    <li
      onClick={() => props.somefunction(props.id)}
      // style={{ textDecoration: strikeEvent ? "line-through" : "none" }}
    >
      {props.meep}
    </li>
  );
}
