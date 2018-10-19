# Prisoner's Dilemma

### Background
The Prisoner's Dilemma is a classic game theory problem. The fundamental problem is whether or not two rational individuals should collaborate or not given a specific circumstance, namely, the prisoner's dilemma. The problem was originally posed as follows:
  Two members of a criminal gang are arrested and imprisoned. Each prisoner is in solitary confinement with no means of communicating with the other. The prosecutors lack sufficient evidence to convict the pair on the principal charge, but they have enough to convict both on a lesser charge. Simultaneously, the prosecutors offer each prisoner a bargain. Each prisoner is given the opportunity either to betray the other by testifying that the other committed the crime, or to cooperate with the other by remaining silent. The offer is:
    - If A and B each betray the other, each of them serves two years in prison
    - If A betrays B but B remains silent, A will be set free and B will serve three years in prison (and vice versa)
    - If A and B both remain silent, both of them will only serve one year in prison (on the lesser charge).
It is assumed that both prisoners understand the nature of the game, have no loyalty to each other, and will have no opportunity for retribution or reward outside the game. Regardless of what the other decides, each prisoner gets a higher reward by betraying the other ("defecting"). The reasoning involves an argument by dilemma: B will either cooperate or defect. If B cooperates, A should defect, because going free is better than serving 1 year. If B defects, A should also defect, because serving 2 years is better than serving 3. So either way, A should defect. Parallel reasoning will show that B should defect.

Because defection always results in a better payoff than cooperation regardless of the other player's choice, it is a dominant strategy. Mutual defection is the only strong Nash equilibrium in the game (i.e. the only outcome from which each player could only do worse by unilaterally changing strategy). The dilemma, then, is that mutual cooperation yields a better outcome than mutual defection but is not the rational outcome because the choice to cooperate, from a self-interested perspective, is irrational.

### Iterated Prisoner's Dilemma
If two players play prisoner's dilemma more than once in succession and they remember previous actions of their opponent and change their strategy accordingly, the game is called iterated prisoner's dilemma.

The iterated prisoner's dilemma game is fundamental to some theories of human cooperation and trust. On the assumption that the game can model transactions between two people requiring trust, cooperative behavior in populations may be modeled by a multi-player, iterated, version of the game. It has, consequently, fascinated many scholars over the years. In 1975, Grofman and Pool estimated the count of scholarly articles devoted to it at over 2,000. The iterated prisoner's dilemma has also been referred to as the "Peace-War game".

If the game is played exactly N times and both players know this, then it is optimal to defect in all rounds. The only possible Nash equilibrium is to always defect. The proof is inductive: one might as well defect on the last turn, since the opponent will not have a chance to later retaliate. Therefore, both will defect on the last turn. Thus, the player might as well defect on the second-to-last turn, since the opponent will defect on the last no matter what is done, and so on. The same applies if the game length is unknown but has a known upper limit.

Unlike the standard prisoner's dilemma, in the iterated prisoner's dilemma the defection strategy is counter-intuitive and fails badly to predict the behavior of human players. Within standard economic theory, though, this is the only correct answer. The superrational strategy in the iterated prisoner's dilemma with fixed N is to cooperate against a superrational opponent, and in the limit of large N, experimental results on strategies agree with the superrational version, not the game-theoretic rational one.

For cooperation to emerge between game theoretic rational players, the total number of rounds N must be unknown to the players. In this case 'always defect' may no longer be a strictly dominant strategy, only a Nash equilibrium. Amongst results shown by Robert Aumann in a 1959 paper, rational players repeatedly interacting for indefinitely long games can sustain the cooperative outcome.

### Resources
- [Wiki](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma#Generalized_form)
