import './index.css'
import React, {useState} from "react"
import NavigationBar from './components/navigationBar'
import Game from './components/game'
import Timer from './components/timer'

function App() {
  const [myProps, setMyProps] = useState({
    player1Color: "#0000FF",
    player2Color: "#FF0000",
    boardColor: "#00FF00",
    backgroundColor: "#FFFFFF",
    player1PieceStyle: "style1",
    player2PieceStyle: "style1",
    boardStyle: "style1",
    backgroundStyle: "style1",
    pieceStyles: ["style1", "style2", "style3"],
    boardStyles: ["style1", "style2", "style3"],
    backgroundStyles: ["style1", "style2", "style3"],
    selectedSpot: [-1, -1],
    currPlayerID: 1
  })
  console.log(myProps)

  const updateMyProps = (newProps) => {
    setMyProps({...myProps, ...newProps})
  }

  return (
    <div className="app" >
      <NavigationBar myProps={myProps} updateMyProps={updateMyProps} />
      <Game myProps={myProps} updateMyProps={updateMyProps} />
      <Timer myProps={myProps} updateMyProps={updateMyProps} />
    </div>
  )
}

export default App
