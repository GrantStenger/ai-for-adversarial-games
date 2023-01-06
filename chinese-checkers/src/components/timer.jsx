import "../index.css"

export default function Timer({myProps, updateMyProps}) {
    return (
        <div className="timer" >
            <p>I am TIMER</p>
            <p>{(myProps.winner === 1 && "You win!") || (myProps.winner === 2 && "You lost, better luck next time") || (myProps.winner === 0 && "Game on!")}</p>
        </div>
    )
}