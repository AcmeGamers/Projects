import React, { useState } from "react";
import AddIcon from "@material-ui/icons/Add";
import Fab from "@material-ui/core/Fab";
import Zoom from "@material-ui/core/Zoom";

export default function CreateArea(props) {
  // For holding values of notes
  const [note, setNote] = useState({
    title: "",
    content: ""
  });

  // Assinging them as complete product to the list array
  function handleChange(event) {
    const { name, value } = event.target;

    setNote((prevNote) => {
      return {
        ...prevNote,
        [name]: value
      };
    });
  }

  // On Sumbit, it will prevent default flow of form and
  // Add a note.
  function submitNote(event) {
    props.onAdd(note);
    setNote({
      title: "",
      content: ""
    });
    event.preventDefault();
  }

  // Until Textarea is clicked, input, button is hidden
  // And textarea row is set to 1
  var [textAreaState, setTextAreaState] = useState({
    inputState: false,
    buttonState: false,
    rows: 1
  });

  // Function to change states upon
  function updateTextAreaState(event) {
    const { name } = event.target;
    // console.log(value, name);
    // setTextAreaState((() => [name]: value));
    setTextAreaState(() => {
      if (name === "content") {
        return {
          inputState: true,
          buttonState: true,
          rows: 4
        };
      }
    });
  }

  // Returning Data
  return (
    <div>
      <form className="create-note">
        {textAreaState.inputState && (
          <input
            name="title"
            onChange={handleChange}
            value={note.title}
            placeholder="Title"
          />
        )}
        <textarea
          onClick={updateTextAreaState}
          name="content"
          onChange={handleChange}
          value={note.content}
          placeholder="Take a note..."
          rows={textAreaState.rows}
        />
        <Zoom in={textAreaState.buttonState}>
          <Fab color="secondary" onClick={submitNote}>
            <AddIcon />
          </Fab>
        </Zoom>
      </form>
    </div>
  );
}
