# Exercise 4: AI as Learning Amplifier

## Goal
Learn about wireless routing protocols the RIGHT way - try first, then use AI to help

---

## Phase 1: My Own Learning (No AI!)

### What I read (about 2 hours):
- Wikipedia pages on routing protocols
- Some Cisco documentation
- Random blog posts about OSPF and RIP

### What I understood:

**Routing protocols = rules that help routers talk to each other**

They share information about the network so routers know where to send data. Without them, you'd have to manually configure every route.

**Main types I learned:**

1. **RIP** - Simple and old. Just counts hops (how many routers to pass through). Max 15 hops. Easy to set up but kinda dumb - doesn't care if a link is slow.

2. **OSPF** - Smarter. Builds a complete map of the network and calculates best paths. Uses bandwidth to decide what's "best" not just hop count. Good for bigger networks.

3. **BGP** - Runs the whole internet. Super complex. Connects different organizations. I don't fully get this one yet.

4. **Wireless protocols (AODV, OLSR):**
   - AODV = finds routes only when needed (saves battery)
   - OLSR = always maintains routes (faster but uses more power)

**Key idea I got:**
Battery powered devices need different protocols than plugged-in routers. Mobile devices need different protocols than stationary ones.

### Self-test (closed all docs):

**How does OSPF work?**
Each router sends messages to everyone saying "here's what I'm connected to". All routers collect this info and build identical maps of the network. Then they each calculate shortest paths from the map.

**When would I use each protocol?**
- RIP: tiny network, like home or small office
- OSPF: company network with lots of routers
- BGP: connecting to internet or between companies
- AODV: battery powered sensors that move around
- OLSR: wireless devices that don't move and have power

### Simple scenario I designed:

**Coffee shop network:**
- 1 main router (to internet)
- 3 WiFi access points
- 5 office computers
- 1 server
- Guest WiFi

**What protocol?**
Actually... none! Network is too small. Just use static routes or even just switches/VLANs. The router just needs default route to ISP.

**What could fail?**
- If main router dies, everything down
- No backup internet
- If I mess up VLANs, guests might access business stuff

---

## Phase 2: Using AI Strategically

### Testing myself:

**I asked AI:** "Quiz me on OSPF with 3 questions"

**AI asked:**
1. How does OSPF calculate routes differently than RIP?
2. What are OSPF areas for?
3. How does OSPF detect link failures?

**My answers:**
1. OSPF uses full network map and considers bandwidth. RIP just counts hops.
2. Areas divide big networks into sections... to reduce overhead I think?
3. Uses hello messages. If router stops responding, link is dead.

**AI feedback:**
Mostly right! AI explained areas also help with route summarization which I didn't know. Also said OSPF convergence is fast but depends on network size.

### Exploring edge cases:

**I asked:** "What if a link keeps going up and down quickly?"

**AI explained:**
OSPF has throttling so it doesn't recalculate routes constantly. Without this the whole network would be unstable. Cool - I didn't think about this!

**I asked:** "For 500 battery-powered sensors sending data once per hour, reactive or proactive routing?"

**My guess:** Reactive (AODV) because battery matters and they barely send data.

**AI said:** Good reasoning! But also mentioned specialized IoT protocols like RPL that are even better. And maybe don't need full routing - could just use tree structure to gateway.

This made me realize: for specific use cases there are specialized protocols I don't know about yet.

---

## Phase 3: Real Application - Smart City

**Design requirements:**
- 1,000 IoT sensors
- 50 traffic lights
- 10 emergency vehicles

### My design:

**Architecture:**
3 layers:
- Sensors → Gateways (10 gateways, 100 sensors each)
- Gateways → Fog computing nodes (3 nodes for redundancy)
- Fog nodes → Cloud datacenter

**Protocols I chose:**

**Sensors to gateways:** Simple tree routing or RPL
- Why: battery powered, send data rarely, don't need complex routing
- Just report to nearest gateway and sleep

**Gateways to fog nodes:** OSPF
- Why: need fast failover if fog node dies
- Gateways have power, can handle overhead
- Only 10 gateways so not too complex

**Traffic lights:** OLSR (proactive mesh)
- Why: powered by grid, need instant response
- Don't move so stable topology
- Mesh gives redundancy for safety

**Emergency vehicles:** LTE cellular + fog nodes
- Why: they move around constantly
- Use regular cellular network mostly
- City network as backup

### Failure scenarios:

**Fog node fails:**
OSPF reroutes gateways to different fog node in seconds. Might lose some sensor data during switch but recovers automatically.

**Vehicle loses signal:**
Falls back to LTE. Caches recent data locally. Traffic lights still work independently if needed.

**Traffic lights lose power:**
Mesh routes around failed section. Failed lights use timer-based fallback. Self-heals when power returns.

### AI feedback on my design:

**I asked AI:** "What critical issues did I miss?"

**AI pointed out:**
- Security! Need encryption especially for traffic lights
- QoS - emergency traffic must be prioritized over sensors
- Bandwidth - if traffic lights send video, might overwhelm network
- Time sync needed for traffic coordination
- Need monitoring system to detect problems

**What I added:**
- QoS with emergency priority
- Encryption for safety-critical systems
- Data aggregation at gateways (don't send raw sensor data)
- Network monitoring
- Separate VLANs for different traffic types

---

## Reflection

### Human vs AI contribution:
- Phase 1: 100% me
- Phase 2: 70% me, 30% AI (I asked questions, AI filled gaps)
- Phase 3: 75% me, 25% AI (I designed it, AI caught what I missed)

**Overall: about 80% my work, 20% AI helping**

### Can I defend my design without AI?
Yes! I know WHY I chose each protocol:
- Tree routing for sensors = battery life
- OSPF for gateways = fast failover
- OLSR for traffic lights = real-time needs
- Hierarchical layers = scalability

I understand the trade-offs and can explain alternatives.

### What will I remember in 6 months?
- Reactive vs proactive (battery vs speed)
- OSPF good for fast convergence
- Hierarchical design for scaling
- IoT needs specialized protocols
- Security and QoS matter as much as routing choice

I'll remember because I struggled through it myself and applied it.

### Did AI make me sharper or think for me?

**Made me sharper.**

I came to AI WITH ideas and questions, not FOR ideas. AI showed me gaps and edge cases I missed. But the core learning and design was mine.

If I'd just asked "explain routing protocols" at the start, I'd have nice notes but zero real understanding. Couldn't design anything or make trade-offs.