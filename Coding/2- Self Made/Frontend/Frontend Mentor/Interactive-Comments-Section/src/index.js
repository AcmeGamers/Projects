import React, { useRef } from "react";
import ReactDOM from "react-dom";

function Card(props) {
  return (
    <div>
      <div className={"card row " + props.class}>
        <div className="column upvoting vr-center hr-center">
          <a href="#">+</a>
          <span>{props.score}</span>
          <a href="#">-</a>
        </div>

        <div>
          <div className="row space-between hr-center">
            <div className="user-info row hr-center">
              <img
                className="user"
                src="./images/avatars/image-amyrobson.png"
                alt=""
              />
              <a className="username mg-lr-15px">{props.username}</a>
              <p className="period">{props.createdAt}</p>
            </div>
            <button className="btn btn-reply">
              <img src="./images/icon-reply.svg" /> Reply
            </button>
          </div>
          <p className="comment">{props.content}</p>
        </div>
      </div>
      {props.children && (
        <div className="card-reply-container column hr-right">
          {props.children}
        </div>
      )}
    </div>
  );
}
function CardReply(props) {
  return (
    <Card
      key={props.id}
      score={props.score}
      username={props.username}
      createdAt={props.createdAt}
      content={props.content}
      class="card-reply"
    />
  );
}
function CommentCard(props) {
  let userComment = useRef("");
  return (
    <div className="card row vr-top space-between">
      <img className="user" src={props.image} alt="" />
      <textarea
        name="text"
        type="text"
        placeholder="Add a comment..."
        className="mg-lr-10px"
        cols="30"
        rows="10"
        useRef={userComment}
      ></textarea>
      <button
        className="btn btn-send"
        onClick={() => {
          databaseData.comments.push({
            id: 1,
            content: userComment.current,
            createdAt: "12 secs",
            score: 0,
            user: {
              image: {
                png: currentUser.image.png,
                webp: currentUser.image.webp,
              },
              username: currentUser.username,
            },
            replies: [],
          });
          console.log(databaseData.comments[databaseData.comments.length - 1]);
        }}
      >
        Send
      </button>
    </div>
  );
}

let currentUser = {
    image: {
      png: "./images/avatars/image-juliusomo.png",
      webp: "./images/avatars/image-juliusomo.webp",
    },
    username: "juliusomo",
  },
  databaseData = {
    comments: [
      {
        id: 1,
        content:
          "Impressive! Though it seems the drag feature could be improved. But overall it looks incredible. You've nailed the design and the responsiveness at various breakpoints works really well.",
        createdAt: "1 month ago",
        score: 12,
        user: {
          image: {
            png: "./images/avatars/image-amyrobson.png",
            webp: "./images/avatars/image-amyrobson.webp",
          },
          username: "amyrobson",
        },
        replies: [],
      },
      {
        id: 2,
        content:
          "Woah, your project looks awesome! How long have you been coding for? I'm still new, but think I want to dive into React as well soon. Perhaps you can give me an insight on where I can learn React? Thanks!",
        createdAt: "2 weeks ago",
        score: 5,
        user: {
          image: {
            png: "./images/avatars/image-maxblagun.png",
            webp: "./images/avatars/image-maxblagun.webp",
          },
          username: "maxblagun",
        },
        replies: [
          {
            id: 3,
            content:
              "If you're still new, I'd recommend focusing on the fundamentals of HTML, CSS, and JS before considering React. It's very tempting to jump ahead but lay a solid foundation first.",
            createdAt: "1 week ago",
            score: 4,
            replyingTo: "maxblagun",
            user: {
              image: {
                png: "./images/avatars/image-ramsesmiron.png",
                webp: "./images/avatars/image-ramsesmiron.webp",
              },
              username: "ramsesmiron",
            },
          },
          {
            id: 4,
            content:
              "I couldn't agree more with this. Everything moves so fast and it always seems like everyone knows the newest library/framework. But the fundamentals are what stay constant.",
            createdAt: "2 days ago",
            score: 2,
            replyingTo: "ramsesmiron",
            user: {
              image: {
                png: "./images/avatars/image-juliusomo.png",
                webp: "./images/avatars/image-juliusomo.webp",
              },
              username: "juliusomo",
            },
          },
        ],
      },
    ],
  };

function App() {
  return (
    <div>
      {databaseData.comments.map((record) => (
        <Card
          key={record.id}
          score={record.score}
          username={record.username}
          createdAt={record.createdAt}
          content={record.content}
        >
          {record.replies == []
            ? ""
            : record.replies.map((reply) => (
                <CardReply
                  key={reply.id}
                  score={reply.score}
                  username={reply.username}
                  createdAt={reply.createdAt}
                  content={reply.content}
                />
              ))}
        </Card>
      ))}
      <CommentCard image={currentUser.image.png} />
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
