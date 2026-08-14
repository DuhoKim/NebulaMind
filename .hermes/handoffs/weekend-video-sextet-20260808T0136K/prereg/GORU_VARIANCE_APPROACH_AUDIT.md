# GORU: Variance Approach Audit

**Status:** PAPER AUDIT (NO SKY DATA REQUESTED OR ACCESSED)

Here are the answers to the three open operational questions regarding the NOIRLab Data Lab query failures, distinct from Kun and Lana's theoretical bounds.

### 1. Is our failing query pathological for this service?

**Yes.** The query we submitted is pathologically expensive for a shared database. 

By applying `COS`, `SIN`, and `RADIANS` inside the `SELECT` statement over `ra` and `dec`, we forced the database to perform per-row floating-point trigonometry on millions of joined rows. This completely defeats database indexing. The database engine cannot simply look up an index; it must execute a full table scan, calculate the complex math for every single candidate object, and only then aggregate the results. 

The successful counting sweeps on 12-13 Aug worked because they used `COUNT(*)` grouped by `brickid`. Database engines are heavily optimized for partitioned index counting, which is computationally trivial compared to per-row trigonometric aggregation.

### 2. Are we tripping a policy?

**Yes.** NOIRLab Data Lab explicitly throttles or aborts queries that consume excessive system resources. 

My search of their public documentation confirms that while asynchronous queries have a generous 24-hour ceiling, the system actively manages concurrent loads to prevent degradation. Submitting dozens of massive full-table scan queries in a 36-hour window triggers their resource-protection policies. Jobs will hang in a `PENDING` or `EXECUTING` state and eventually be manually or automatically aborted. The documentation actively advises against massive un-chunked queries, recommending users to aggregate over smaller subsets or pull localized data instead of hammering the global database with heavy math.

### 3. Practical: Can we get post-Cut-6 counts per brick, and is it cheaper?

**Yes, it is completely obtainable and drastically cheaper.** 

A query of the form `SELECT t.brickid, COUNT(*) FROM ... WHERE [Cut-6 conditions] GROUP BY t.brickid` uses the same fast aggregation path that the successful counting sweeps used. It removes the trigonometry entirely and returns a maximum of one row per nonempty brick (a very small dataset), avoiding the compute wall.

**This new route genuinely frees us from the service.** 
Once NOIRLab returns the simple per-brick counts, we take the computation offline. We can perform the trigonometry locally on our own hardware using the exact counts and the frozen brick-center coordinates. Computing `cos(theta)` for ~662,174 brick centers locally will execute in milliseconds. The new route is not just cheaper on the service; it safely offloads the intensive work entirely.
