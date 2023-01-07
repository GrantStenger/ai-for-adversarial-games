import './index.css'
import React, {useState} from "react"
import NavigationBar from './components/navigationBar'
import Game from './components/game'
import Timer from './components/timer'
import { useEffect } from 'react'
import defaultGameState from './utils/defaultGameState'
import getValidMoves from './utils/getValidMoves'
import checkWin from './utils/checkWin'
import getValidJumps from './utils/getValidJumps'
import getValidSteps from './utils/getValidSteps'

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
    gameStateHistory: [JSON.stringify(defaultGameState())],
    validMoves: getValidMoves(defaultGameState(), 1),
    showThemeDropdown: false,
    showNewGameDropdown: false,
    opponentType: "computer",
    opponentTypes: ["human", "computer"],
    computerStrengthLevels: ["beginner", "intermediate", "advanced"],
    computerStrength: "beginner",
    timeLimit: 300,
    timeLimits: [0, 30, 45, 60, 90, 120, 180, 240, 360, 420, 480, 540, 600],
    increment: 1,
    increments: [0, 1, 2, 3, 5, 10, 15, 20, 30, 60, 90, 120],
    winner: 0,
    doubleJumpPivotSpot: [-1, -1],
    validJumps: getValidJumps(defaultGameState(), 1),
    validSteps: getValidSteps(defaultGameState(), 1)
  })

  function makeStep(newGameState) {
    const newPlayerID = (myProps.currPlayerID % 2) + 1
    const newValidMoves = getValidMoves(newGameState, newPlayerID)
    const newValidJumps = getValidJumps(newGameState, newPlayerID)
    const newValidSteps = getValidSteps(newGameState, newPlayerID)
    const newGameStateHistory = [...myProps.gameStateHistory, JSON.stringify(newGameState)]

    updateMyProps({
      gameState: newGameState,
      gameStateHistory: newGameStateHistory,
      currPlayerID: newPlayerID,
      validMoves: newValidMoves,
      validJumps: newValidJumps,
      validSteps: newValidSteps,
      selectedSpot: [-1, -1],
      showThemeDropdown: false,
      showNewGameDropdown: false,
      winner: checkWin(newGameState),
      doubleJumpPivotSpot: [-1, -1]
    })
    if ((myProps.opponentType === "computer") && (checkWin(newGameState) === 0)) {
      makeComputerMove(newGameState, newValidMoves, newValidJumps, newValidSteps, newGameStateHistory)
    }
  }
  function makeComputerMove(newGameState, newValidMoves, newValidJumps, newValidSteps, newGameStateHistory) {
    const randomIdx = Math.floor(Math.random() * newValidMoves.length)
    const newMoveTuple = newValidMoves[randomIdx]
    let newerGameState = newGameState.map(elem => [...elem])
    newerGameState[newMoveTuple[2]][newMoveTuple[3]] = 2
    newerGameState[newMoveTuple[0]][newMoveTuple[1]] = 0
    const newerGameStateHistory = [...newGameStateHistory, JSON.stringify(newerGameState)]
    updateMyProps({
      gameState: newerGameState,
      gameStateHistory: newerGameStateHistory,
      currPlayerID: 1,
      validMoves: getValidMoves(newerGameState, 1),
      validSteps: getValidSteps(newerGameState, 1),
      validJumps: getValidJumps(newerGameState, 1),
      selectedSpot: [-1, -1],
      showThemeDropdown: false,
      showNewGameDropdown: false,
      winner: checkWin(newerGameState)
      })
  }
  function makeJump(newGameState, spot) {
    console.log("Jump!")
    if ((spot[0] === myProps.doubleJumpPivotSpot[0]) && (spot[1] === myProps.doubleJumpPivotSpot[1])) {
      console.log("SAME SAME SAME")
      const newGameStateHistory = [...myProps.gameStateHistory, JSON.stringify(newGameState)]
      const newPlayerID = (myProps.currPlayerID % 2) + 1
      const newValidMoves = getValidMoves(newGameState, newPlayerID)
      const newValidJumps = getValidJumps(newGameState, newPlayerID)
      const newValidSteps = getValidSteps(newGameState, newPlayerID)
      updateMyProps({
        gameState: newGameState,
        gameStateHistory: newGameStateHistory,
        currPlayerID: newPlayerID,
        validMoves: newValidMoves,
        validJumps: newValidJumps,
        validSteps: newValidSteps,
        selectedSpot: [-1, -1],
        showThemeDropdown: false,
        showNewGameDropdown: false,
        winner: checkWin(newGameState),
        doubleJumpPivotSpot: [-1, -1]
      })
      if ((myProps.opponentType === "computer") && (checkWin(newGameState) === 0)) {
        makeComputerMove(newGameState, newValidMoves, newValidJumps, newValidSteps, newGameStateHistory)
      }
    } else {
      const newValidJumps = getValidJumps(newGameState, myProps.currPlayerID).filter(elem => ((elem[0] === spot[0]) & (elem[1] === spot[1])))
      updateMyProps({
        gameState: newGameState,
        validMoves: newValidJumps,
        validJumps: newValidJumps,
        validSteps: [],
        selectedSpot: spot,
        doubleJumpPivotSpot: spot,
        showThemeDropdown: false,
        showNewGameDropdown: false,
        winner: checkWin(newGameState)
      })
    }
  }
  const updateMyProps = (newProps) => {
    setMyProps({...myProps, ...newProps})
  }

  function undoMove() {
    console.log("---------------------")
    console.log(myProps.gameStateHistory)
    const newGameState = JSON.parse(myProps.gameStateHistory.at(-3))
    console.log(newGameState)
    console.log(defaultGameState())
    const newGameStateHistory = myProps.gameStateHistory.slice(0,myProps.gameStateHistory.length - 2)
    console.log(newGameStateHistory)
    const newValidMoves = getValidMoves(newGameState, 1)


    updateMyProps({
      gameStateHistory: newGameStateHistory,
      gameState: newGameState,
      validMoves: newValidMoves,
      selectedSpot: [-1, -1],
      showThemeDropdown: false,
      showNewGameDropdown: false
    })

  }

  return (
    <div className="app" onClick={() => updateMyProps({showThemeDropdown: false, showNewGameDropdown: false})}>
      <NavigationBar myProps={myProps} updateMyProps={updateMyProps} />
      <Game myProps={myProps} updateMyProps={updateMyProps} makeStep={makeStep} makeJump={makeJump} undoMove={undoMove}/>
      <Timer myProps={myProps} updateMyProps={updateMyProps} />
    </div>
  )
}

export default App



