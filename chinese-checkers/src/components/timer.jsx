import "../index.css"
import aiDark from "../assets/aiDark.svg"
import aiLight from "../assets/aiLight.svg"
import man1 from "../assets/man1.svg"
import man2 from "../assets/man2.svg"
import { useEffect, useState } from "react"

export default function Timer({myProps, updateMyProps}) {
    const [tempTimeLeftPlayer1, setTempTimeLeftPlayer1] = useState(myProps.timeLeftPlayer1)
    const [tempTimeLeftPlayer2, setTempTimeLeftPlayer2] = useState(myProps.timeLeftPlayer2)
    useEffect(() => {
        if (!tempTimeLeftPlayer1) {
            console.log("Player 1 is out of time")
            return
        } else if (!tempTimeLeftPlayer2) {
            console.log("Player 2 is out of time")
            return
        } else  {
            const intervalId = setInterval(() => {
                if (myProps.currPlayerID === 1) {
                    setTempTimeLeftPlayer1(myProps.timeLeftPlayer1 - (Date.parse(new Date()) - myProps.dateBenchmark))
                } else {
                    setTempTimeLeftPlayer2(myProps.timeLeftPlayer2 - (Date.parse(new Date()) - myProps.dateBenchmark))
                }
            }, 1000)
        }
    }, [tempTimeLeftPlayer1, tempTimeLeftPlayer2])
    const farProfileImg = myProps.opponentType === "computer" ? aiDark : man2
    return (
        <div className="timer" >
            {/* <div className="farTimer"><div className="indicator" state={myProps.currPlayerID === 1 ? "off" : "on"}></div><p>1:18</p></div> */}
            <div className="farTimer"><div className="indicator" state={myProps.currPlayerID === 1 ? "off" : "on"}></div><p>{tempTimeLeftPlayer2}</p></div>
            <div className="farProfile"><figure><img src={farProfileImg} height="25px" width="25px" /></figure><p>Jeff</p></div>
            <div className="nearProfile"><figure><img src={man1} height="25px" width="25px" /></figure><p>Greg</p></div>
            {/* <div className="nearTimer"><div className="indicator" state={myProps.currPlayerID === 1 ? "on" : "off"}></div><p>2:32</p></div> */}
            <div className="nearTimer"><div className="indicator" state={myProps.currPlayerID === 1 ? "on" : "off"}></div><p>{tempTimeLeftPlayer1}</p></div>
            <p>{(myProps.winner === 1 && "You win!") || (myProps.winner === 2 && "You lost, better luck next time") || (myProps.winner === 0 && "Game on!")}</p>
        </div>
    )
}