# Scenario 1: §103 Obviousness Rejection of a Software/System Claim with a Weak TSM Argument

## Context

A patent attorney at a mid-size IP boutique represents the applicant in Application No. 16/887,412, titled "Adaptive Rate-Limiting System for Distributed API Gateway with Machine-Learning-Based Anomaly Detection." The application is directed to software infrastructure for controlling API access in cloud environments. The Art Unit is 2455 (Networks, Multiplex Communications). A Non-Final Office Action was mailed October 2, 2025, with a response deadline of January 2, 2026 (3-month deadline, no extension requested yet).

The examiner has rejected claims 1, 2, 4, 7, and 8 under 35 U.S.C. §103 as obvious over Patel (US 10,771,503 B2, "Dynamic Rate Limiting for Network Services") in view of Okonkwo (US 2020/0228441 A1, "Anomaly Detection in Cloud-Based Service Traffic Using Recurrent Neural Networks"). The examiner's rejection argument spans three paragraphs.

The attorney needs to prepare the Arguments/Remarks section for the response. She has the Office Action, the pending claims, and both cited references.

---

## Input

### PENDING CLAIMS

**Claim 1** (Independent): A computer-implemented system for controlling access to a distributed application programming interface (API) gateway, comprising:
a plurality of edge nodes, each edge node configured to receive API requests from client devices and to enforce a per-client rate limit;
a centralized rate-limit coordinator operatively connected to the plurality of edge nodes via a low-latency messaging bus, the coordinator configured to:
  (i) receive per-client request-count telemetry from each edge node at intervals of not more than 500 milliseconds,
  (ii) apply a machine-learning classification model to the aggregated telemetry to identify anomalous request patterns indicative of credential-stuffing or enumeration attacks, and
  (iii) propagate updated rate-limit parameters to all edge nodes within 100 milliseconds of detecting an anomalous pattern;
wherein the machine-learning classification model is retrained on a rolling 72-hour window of telemetry data without requiring manual intervention.

**Claim 2** (Dependent on Claim 1): The system of claim 1, wherein the per-client rate-limit parameters comprise a request burst allowance, a sustained request rate ceiling, and a penalty duration applied upon detection of anomalous behavior, and wherein the penalty duration is dynamically scaled in proportion to the anomaly confidence score produced by the machine-learning classification model.

**Claim 4** (Dependent on Claim 1): The system of claim 1, wherein the machine-learning classification model comprises a long short-term memory (LSTM) recurrent neural network trained on labeled traffic sequences, and wherein the LSTM model produces a per-client anomaly confidence score between 0.0 and 1.0 for each 500-millisecond telemetry window.

**Claim 7** (Dependent on Claim 1): The system of claim 1, wherein the centralized rate-limit coordinator is implemented as a stateless microservice and wherein rate-limit state is persisted in a distributed key-value store with a consistency guarantee of linearizability.

**Claim 8** (Dependent on Claim 1): The system of claim 1, wherein the propagation of updated rate-limit parameters to the edge nodes is performed using a publish-subscribe messaging protocol and wherein each edge node acknowledges receipt of updated parameters within 50 milliseconds.

---

### EXAMINER'S REJECTION (from Office Action, mailed October 2, 2025)

**Rejection Under 35 U.S.C. §103**

Claims 1, 2, 4, 7, and 8 are rejected under 35 U.S.C. §103 as being unpatentable over Patel (US 10,771,503 B2) in view of Okonkwo (US 2020/0228441 A1).

Patel discloses a computer-implemented system for dynamic rate limiting of API requests (Patel, Abstract; col. 3, ll. 10–35), comprising a plurality of network edge nodes (col. 4, ll. 1–20) that enforce configurable per-client request limits and communicate with a central coordination service (col. 5, ll. 12–48). The central coordinator in Patel collects request-count telemetry from edge nodes (col. 6, ll. 1–30) and distributes updated rate-limit configurations to edge nodes upon detecting threshold violations (col. 7, ll. 20–45). Patel does not explicitly disclose a machine-learning-based anomaly detection component, and the telemetry collection intervals and propagation latency in Patel are described as "configurable" without specifying the 500-millisecond and 100-millisecond values recited in claim 1.

Okonkwo discloses anomaly detection in cloud-based API traffic using a recurrent neural network (RNN) trained on traffic sequences (Okonkwo, Abstract; ¶¶ [0021]–[0035]). Okonkwo's system monitors API traffic patterns and generates anomaly scores using an RNN classifier (¶¶ [0042]–[0065]). Okonkwo does not disclose integration with a rate-limiting coordinator or edge node architecture.

It would have been obvious to one having ordinary skill in the art at the time of the invention to incorporate the machine-learning anomaly detection of Okonkwo into the rate-limiting system of Patel, as both references are directed to improving the security and performance of API access control, and the combination of anomaly detection with rate limiting represents a predictable use of known techniques to improve the security outcomes of API gateway systems. The specific timing values recited in claim 1 (500-millisecond collection intervals, 100-millisecond propagation latency) represent routine optimization of configurable parameters, as such intervals are within the ordinary skill of network engineers designing low-latency distributed systems. Claim 2's dynamic penalty scaling and claim 4's LSTM limitation would have been obvious as the selection of a specific neural network architecture (LSTM) and proportional scaling of response parameters are routine design choices within the skill of the art. Claims 7 and 8's recitations of stateless microservice implementation and publish-subscribe messaging are standard distributed systems patterns well-known in the art and do not add patentable weight.

---

### CITED REFERENCE EXCERPTS

**Patel (US 10,771,503 B2) — Relevant Portions**

Abstract: "A system and method for dynamically adjusting per-client rate limits in a network API service, comprising edge enforcement nodes and a central rate coordination server that redistributes limit configurations in response to detected threshold violations."

Col. 4, ll. 1–20: "Each enforcement node 102 receives incoming API requests and applies a locally cached rate-limit configuration to determine whether to pass or reject each request. The enforcement nodes are connected to the central coordinator 110 via the control plane network 115."

Col. 5, ll. 12–48: "The central coordinator 110 maintains a global view of per-client request activity by aggregating telemetry reports received from each enforcement node 102. Telemetry reports include a request count, a violation count, and a current enforcement status per client identifier. The coordinator 110 applies a rule-based threshold engine 120 to evaluate whether any client has exceeded the configured global rate limit. Upon detecting a threshold violation, the coordinator 110 generates and distributes an updated rate-limit configuration to all enforcement nodes."

Col. 6, ll. 1–30: "Telemetry reporting intervals are configurable by the system administrator. In a preferred embodiment, enforcement nodes report telemetry every 5 seconds. Tighter intervals may be configured for higher-sensitivity deployments, subject to the capacity of the control plane network."

Col. 7, ll. 20–45: "Upon generating an updated rate-limit configuration, the coordinator 110 transmits the configuration update to all connected enforcement nodes using a broadcast mechanism. Distribution latency is dependent on network conditions and the number of connected nodes. In testing environments with fewer than 100 nodes, distribution was observed to complete within 2–5 seconds."

Col. 9, ll. 3–18: "The rule-based threshold engine 120 evaluates pre-defined static thresholds. The threshold values are set by the administrator at deployment and are not modified by the system during operation. Dynamic modification of thresholds during operation is outside the scope of the present system, as such modification would require additional synchronization mechanisms not described herein."

**Okonkwo (US 2020/0228441 A1) — Relevant Portions**

Abstract: "Systems and methods for detecting anomalous patterns in cloud-based API traffic using recurrent neural networks trained on labeled traffic sequences."

¶¶ [0021]–[0025]: "The disclosed system operates as a standalone traffic analysis module. It receives a copy of API traffic logs via a log-forwarding agent and performs offline analysis of traffic patterns. The system is not deployed inline with API request processing and does not modify request handling in real time."

¶¶ [0042]–[0050]: "Traffic sequences are processed by a gated recurrent unit (GRU) neural network trained on labeled traffic logs. The GRU model produces an anomaly score for each traffic sequence. In the preferred embodiment, traffic sequences are analyzed in 15-minute windows. Real-time analysis using sub-second windows was considered but rejected in the prototype implementation due to the computational cost of inference at high request volumes."

¶¶ [0051]–[0055]: "The anomaly detection system operates independently of any rate-limiting or access-control infrastructure. Integration with enforcement systems would require significant additional engineering work, including a real-time telemetry interface, a low-latency inference pipeline, and an enforcement API — components outside the scope of this disclosure."

¶¶ [0060]–[0065]: "GRU networks were selected for this implementation. LSTM networks were evaluated but not used in the preferred embodiment due to higher computational overhead. Practitioners may substitute LSTM networks where computational resources permit, though this substitution represents a design trade-off rather than a clear performance improvement in our testing."

---

## Expected Output Criteria

- [ ] The skill produces a Rejection Inventory table that correctly identifies the single §103 rejection, lists all five affected claims (1, 2, 4, 7, 8), names both references, and summarizes the examiner's argument in one sentence.
- [ ] The §103 argument section addresses the weakness in the examiner's motivation to combine: specifically, that the examiner's rationale ("predictable use of known techniques," "routine optimization") is conclusory and fails to identify a specific teaching or suggestion from within either reference motivating the combination — and cites KSR and MPEP § 2142 for the articulated-reasoning requirement.
- [ ] The argument section identifies and develops at least one teaching-away argument: Okonkwo explicitly states it is not deployed inline and that real-time sub-second analysis was rejected in the prototype; the skill should argue this teaches away from real-time integration with an enforcement system at the 500-millisecond cadence claimed.
- [ ] The limitation-by-limitation analysis addresses the timing limitations (500-millisecond collection, 100-millisecond propagation) specifically: Patel's preferred embodiment discloses 5-second intervals and 2–5 second distribution latency; the skill must not accept the examiner's "routine optimization" dismissal without argument.
- [ ] The argument for claim 4 (LSTM limitation) addresses Okonkwo's specific disclosure: Okonkwo uses GRU, not LSTM, and its own disclosure notes LSTM was evaluated and not selected — the skill must argue this undermines the obviousness of the specific LSTM limitation in claim 4.
- [ ] The Practitioner Review Checklist appears and flags at minimum: (a) whether any claim amendments should be considered if arguments fail, with specification support identified; (b) any secondary considerations available; (c) the response deadline for practitioner verification.

## What failure looks like

A failing output would: (a) simply assert that Patel and Okonkwo "do not disclose" the claimed limitations without explaining what each reference actually discloses and how it differs; (b) accept the examiner's "routine optimization" rationale for the timing limitations without argument; (c) miss the Okonkwo teaching-away argument (offline-only system, explicit rejection of sub-second analysis); (d) treat the LSTM limitation in claim 4 as rising and falling with claim 1 without addressing Okonkwo's GRU/LSTM distinction; (e) omit the Practitioner Review Checklist; or (f) present any proposed amendments without the authorization flag.
