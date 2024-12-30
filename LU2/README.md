# Assignment: Rational Agents

In this assignment, you will deepen your understanding of rational agents, their performance measures, and utility functions. You will also learn how to describe agents in terms of the PEAS (Performance, Environment, Actuators, Sensors) framework and characterize their operating environments.

---

## A. Performance and Utility

### 1. What is the difference between a performance measure and a utility function?

- **Performance Measure**:  
  A performance measure is an external, objective criterion used by someone (e.g., a designer or evaluator) to determine how successful an agent is in meeting the goals set for it. It essentially tells us how well the agent is performing **from an external viewpoint**.

- **Utility Function**:  
  A utility function is an **internal** evaluation function that an agent uses to decide which actions to take. It maps an agent’s internal state or a possible outcome to a real number, representing the **desirability** of that state from the agent’s own perspective. The agent then **chooses actions** to maximize this utility.

### 2. Describe the relation between the performance measure and the utility function for a learning agent.

For a learning agent:
- The **performance measure** is used by the **critic** (often external or part of the agent's feedback mechanism) to evaluate how well the agent is achieving its design objectives.
- The **utility function** guides the agent’s **learning element** (or decision-making process) by shaping the agent’s preferences.  
- Over time, the agent adjusts its behavior based on the **difference** between how its actions **actually** affect the external performance measure and how its **utility function** **predicted** or evaluated those outcomes.  
- Essentially, **the performance measure is the ultimate yardstick**, while **the agent’s utility function is the internal model** that the agent refines to improve its decisions and better meet the external performance criteria.

---

## B. Rational Agents

### 1. PEAS Descriptions

#### 1.1. Playing Monopoly

- **Performance**:  
  - Acquire the most assets (properties, houses, hotels).  
  - Avoid bankruptcy.  
  - End the game with the highest net worth among players.  

- **Environment**:  
  - The Monopoly board with properties, chance cards, community chest cards, and other players.  
  - Turns proceed in a sequence, and other players' actions (buying, trading, building) affect the game state.  

- **Actuators**:  
  - Actions such as rolling dice, moving the token, buying/selling properties, collecting rent, trading with other players, and deciding when to build houses/hotels.  

- **Sensors**:  
  - Knowledge of the current board state: location of tokens, ownership of properties, houses/hotels built, bank/money status, incoming/outgoing transactions, card draws, etc.

#### 1.2. Spear Throwing Athlete

- **Performance**:  
  - Throw the spear as far as possible.  
  - Achieve accurate aim to land in the designated target area (if relevant for the sport’s scoring).  
  - Minimize fouls or illegal throws.  

- **Environment**:  
  - The field or stadium, weather conditions (wind, temperature, precipitation), and presence of officials or markers.  
  - The athlete’s own physical condition, positioning, and readiness during the competition.  

- **Actuators**:  
  - Muscles and limbs (for running up, gripping, and throwing the spear).  
  - Adjustments to posture, angle of release, and speed.  

- **Sensors**:  
  - Visual feedback (looking at distance markers, target zone), proprioceptive feedback (body position, muscle tension), and possibly coach or environmental cues (wind direction).  

---

### 2. Characterizing the Environments

#### 2.1. Monopoly

1. **Fully Observable vs. Partially Observable**  
   - **Fully Observable (mostly)**: All information (properties, money, positions) is typically open to every player. (Although real-life house rules may obscure some information, the standard game is essentially fully observable.)

2. **Deterministic vs. Stochastic**  
   - **Stochastic**: Dice rolls add an element of randomness, and card draws (Chance, Community Chest) introduce probabilistic elements.

3. **Static vs. Dynamic**  
   - **Static**: The board state only changes when a player takes an action or draws a card on their turn. Nothing changes in between turns due to external forces.

4. **Discrete vs. Continuous**  
   - **Discrete**: The game progresses in turns, and the board has discrete spaces. Money and resource counts are also discrete.

#### 2.2. Spear Throwing Athlete

1. **Fully Observable vs. Partially Observable**  
   - **Partially Observable**: The athlete can observe some aspects of the environment (wind, field conditions, distances), but may not fully know all internal factors (e.g., exact muscle fatigue, precise wind gust changes).

2. **Deterministic vs. Stochastic**  
   - **Stochastic**: Weather conditions (wind gusts), small variations in the athlete’s biomechanics, and other minor unpredictable factors introduce randomness in throw outcomes.

3. **Static vs. Dynamic**  
   - **Dynamic**: Conditions can change during the run-up (e.g., sudden wind shifts), and the athlete’s own movement changes the state of the environment (their position, approach speed, body alignment).

4. **Discrete vs. Continuous**  
   - **Continuous**: Movement, angle of throw, and trajectory happen in a continuous space. Distances are measured in continuous values.

---

## Submission Guidelines

- Submit your answers in a **Markdown** file or a PDF exported from a Markdown editor.  
- Please ensure you **cite** any references if you use external resources beyond your course materials.
- Remember: This is an **individual** assignment. Collaborating or sharing code/answers with classmates is not permitted.

---

**End of Assignment**
