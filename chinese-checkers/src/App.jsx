import './index.css'
import React, {useState} from "react"
import NavigationBar from './components/navigationBar'
import Game from './components/game'
import Timer from './components/timer'
import { useEffect } from 'react'
import defaultGameState from './utils/defaultGameState'
import getValidMoves from './utils/getValidMoves'
import isValidMove from './utils/isValidMove'
import checkWin from './utils/checkWin'


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
    currPlayerID: 1,
    gameState: defaultGameState(),
    validMoves: getValidMoves(defaultGameState(), 1),
    showThemeDropdown: false,
    showNewGameDropdown: false,
    opponentType: ["human", "computer"],
    computerStrengthLevels: ["beginner", "intermediate", "advanced"],
    computerStrength: "beginner",
    timeLimit: 300,
    timeLimits: [0, 30, 45, 60, 90, 120, 180, 240, 360, 420, 480, 540, 600],
    increment: 1,
    increments: [0, 1, 2, 3, 5, 10, 15, 20, 30, 60, 90, 120],
    winner: 0
  })

  function updateGameState(newGameState) {
    const newPlayerID = (myProps.currPlayerID % 2) + 1
    const newValidMoves = getValidMoves(newGameState, newPlayerID)

    updateMyProps({
      gameState: newGameState,
      currPlayerID: newPlayerID,
      validMoves: newValidMoves,
      selectedSpot: [-1, -1],
      showThemeDropdown: false,
      showNewGameDropdown: false,
      winner: checkWin(newGameState)
    })
    
    if ((newPlayerID === 2) && (checkWin(newGameState) === 0)) {
      const randomIdx = Math.floor(Math.random() * newValidMoves.length)
      const newMoveTuple = newValidMoves[randomIdx]
      let newerGameState = [...newGameState]
      newerGameState[newMoveTuple[2]][newMoveTuple[3]] = 2
      newerGameState[newMoveTuple[0]][newMoveTuple[1]] = 0
      updateMyProps({
        gameState: newerGameState,
        currPlayerID: 1,
        validMoves: getValidMoves(newerGameState, 1),
        selectedSpot: [-1, -1],
        showThemeDropdown: false,
        showNewGameDropdown: false,
        winner: checkWin(newerGameState)
      })
    }
  }
  const updateMyProps = (newProps) => {
    setMyProps({...myProps, ...newProps})
  }

  return (
    <div className="app" onClick={() => updateMyProps({showThemeDropdown: false, showNewGameDropdown: false})}>
      <NavigationBar myProps={myProps} updateMyProps={updateMyProps} />
      <Game myProps={myProps} updateMyProps={updateMyProps} updateGameState={updateGameState}/>
      <Timer myProps={myProps} updateMyProps={updateMyProps} />
    </div>
  )
}

export default App



