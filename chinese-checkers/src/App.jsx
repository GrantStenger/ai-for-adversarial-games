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
import isSmallArrayInBigArray from './utils/isSmallArrayInBigArray'

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
    showThemeDropdown: false,
    showNewGameDropdown: false,
    opponentType: "computer",
    opponentTypes: ["human", "computer"],
    computerStrengthLevels: ["beginner", "intermediate", "advanced"],
    computerStrengthLevel: "beginner",
    timeLimit: 300,
    timeLimits: [0, 30, 45, 60, 90, 120, 180, 240, 360, 420, 480, 540, 600],
    increment: 0,
    increments: [0, 1, 2, 3, 5, 10, 15, 20, 30, 60, 90, 120],
    winner: 0,
    doubleJumpPivotSpot: [-1, -1],
    validMoves: getValidMoves(defaultGameState(), 1),
    validJumps: getValidJumps(defaultGameState(), 1),
    validSteps: getValidSteps(defaultGameState(), 1),
    dateBenchmark: Date.parse(new Date()),
    timeLeftPlayer1: 300000,
    timeLeftPlayer2: 300000
  })


  const [tempTimeLeftPlayer1, setTempTimeLeftPlayer1] = useState(myProps.timeLeftPlayer1)
  const [tempTimeLeftPlayer2, setTempTimeLeftPlayer2] = useState(myProps.timeLeftPlayer2)
  
  useEffect(() => {
    if (myProps.timeLimit === 0) {
      console.log("no timer")
      setTempTimeLeftPlayer1(0)
      setTempTimeLeftPlayer2(0)
    } else {
      const intervalId = setInterval(() => {
          if (tempTimeLeftPlayer1 < 0) {
              console.log("Player 1 is out of time")
              setTempTimeLeftPlayer1(0)
              return () => clearInterval(intervalId)
          } else if (tempTimeLeftPlayer2 < 0) {
              console.log("Player 2 is out of time")
              setTempTimeLeftPlayer2(0)
              return () => clearInterval(intervalId)
          } else if (myProps.currPlayerID === 1) {
              setTempTimeLeftPlayer1(myProps.timeLeftPlayer1 - (Date.parse(new Date()) - myProps.dateBenchmark))
          } else {
              setTempTimeLeftPlayer2(myProps.timeLeftPlayer2 - (Date.parse(new Date()) - myProps.dateBenchmark))
          }
      }, 100)
      return () => clearInterval(intervalId)
    }
  }, [myProps])







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
      doubleJumpPivotSpot: [-1, -1],
      dateBenchmark: Date.parse(new Date()),
      timeLeftPlayer1: tempTimeLeftPlayer1,
      timeLeftPlayer2: tempTimeLeftPlayer2
    })
    if ((myProps.opponentType === "computer") && (checkWin(newGameState) === 0)) {
      makeComputerMove(newGameState, newValidMoves, newValidJumps, newValidSteps, newGameStateHistory)
    }
  }
  function makeComputerMove(newGameState, newValidMoves, newValidJumps, newValidSteps, newGameStateHistory) {
    const randomIdx = Math.floor(Math.random() * newValidMoves.length)
    const newMoveTuple = newValidMoves[randomIdx]
    if (isSmallArrayInBigArray(newMoveTuple, newValidSteps)) {
      makeStepComputer(newGameState, newGameStateHistory, newMoveTuple)
    } else {
      var finishedJumping = false
      var newGameStateJumping
      var newMoveTupleJumping
      [finishedJumping, newGameStateJumping, newMoveTupleJumping] = makeJumpComputer(newGameState, newMoveTuple)
      while (finishedJumping === false) {
        [finishedJumping, newGameStateJumping, newMoveTupleJumping] = makeJumpComputer(newGameStateJumping, newMoveTupleJumping)
      }
      const newerGameStateHistoryJumping = [...myProps.gameStateHistory, JSON.stringify(newGameStateJumping)]
      updateMyProps({
        gameState: newGameStateJumping,
        gameStateHistory: newerGameStateHistoryJumping,
        currPlayerID: 1,
        validMoves: getValidMoves(newGameStateJumping, 1),
        validSteps: getValidSteps(newGameStateJumping, 1),
        validJumps: getValidJumps(newGameStateJumping, 1),
        selectedSpot: [-1, -1],
        showThemeDropdown: false,
        showNewGameDropdown: false,
        winner: checkWin(newGameStateJumping),
        dateBenchmark: Date.parse(new Date()),
        timeLeftPlayer1: tempTimeLeftPlayer1,
        timeLeftPlayer2: tempTimeLeftPlayer2
        })
    }
  }
  function makeStepComputer(newGameState, newGameStateHistory, newMoveTuple) {
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
      winner: checkWin(newerGameState),
      dateBenchmark: Date.parse(new Date()),
      timeLeftPlayer1: tempTimeLeftPlayer1,
      timeLeftPlayer2: tempTimeLeftPlayer2
      })
  }
  function makeJumpComputer(newGameState, newMoveTuple) {
    // let newerGameState = newGameState.map(elem => [...elem])
    let newerGameState = [...newGameState]
    newerGameState[newMoveTuple[0]][newMoveTuple[1]] = 0
    newerGameState[newMoveTuple[2]][newMoveTuple[3]] = 2
    // var newerValidJumps = getValidJumps(newerGameState, 2).filter(elem => ((elem[0] === newMoveTuple[2]) && (elem[1] === newMoveTuple[3])))
    const newerValidJumps = [...getValidJumps(newerGameState, 2).filter(elem => ((elem[0] === newMoveTuple[2]) && (elem[1] === newMoveTuple[3]))), [newMoveTuple[2], newMoveTuple[3], newMoveTuple[2], newMoveTuple[3]]]
    updateMyProps({
      gameState: newerGameState,
      validMoves: newerValidJumps,
      validJumps: newerValidJumps,
      validSteps: [],
      selectedSpot: [newMoveTuple[2], newMoveTuple[3]],
      doubleJumpPivotSpot: [newMoveTuple[2], newMoveTuple[3]],
      showThemeDropdown: false,
      showNewGameDropdown: false,
      winner: checkWin(newGameState)
    })
    const randomIdx = Math.floor(Math.random() * newerValidJumps.length)
    const newestMoveTuple = newerValidJumps[randomIdx]
    if ((newestMoveTuple[0] === newestMoveTuple[2]) && (newestMoveTuple[1] === newestMoveTuple[3])) {
      return [true, newerGameState, newestMoveTuple]
    }
    return [false, newerGameState, newestMoveTuple]
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
        doubleJumpPivotSpot: [-1, -1],
        dateBenchmark: Date.parse(new Date()),
        timeLeftPlayer1: tempTimeLeftPlayer1,
        timeLeftPlayer2: tempTimeLeftPlayer2
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
      showNewGameDropdown: false,
      dateBenchmark: Date.parse(new Date()),
      timeLeftPlayer1: tempTimeLeftPlayer1,
      timeLeftPlayer2: tempTimeLeftPlayer2
    })

  }

  return (
    <div className="app" onClick={() => updateMyProps({showThemeDropdown: false, showNewGameDropdown: false})}>
      <NavigationBar myProps={myProps} updateMyProps={updateMyProps} />
      <Game myProps={myProps} updateMyProps={updateMyProps} makeStep={makeStep} makeJump={makeJump} undoMove={undoMove}/>
      <Timer myProps={myProps} updateMyProps={updateMyProps} tempTimeLeftPlayer1={tempTimeLeftPlayer1} tempTimeLeftPlayer2={tempTimeLeftPlayer2}/>
    </div>
  )
}

export default App



