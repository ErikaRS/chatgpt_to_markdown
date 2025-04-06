# Causal Graph Framework

Created: 2025-01-19 16:31:52
Last Updated: 2025-01-19 16:32:18

### User - 2025-01-19 16:31:52

Here's a draft flux lens. Keeping the original as much as possible, make it a bit more rich and FLUX-y

This week’s lens: causal graph.

Amazon popularized the idea of leading indicators as controllable input metrics. In their book Platform Engineering author Camille Fournier and Ian Nowland enrich this idea by connecting it to the idea of a causal graph:

> Imagine constructing a causal graph, where nodes have different inputs you might measure, like storage or experiment throughput, and outputs that are connected to other nodes. Node outputs may be differently sensitive to inputs: maybe the number of experiments you can run increases with throughput at some rate, until you hit diminishing returns because of some other factor. At the end of your graph should be some KPI that’s important to the business, like revenue.

> You should collect impact metrics at the interesting nodes in that graph. … Metrics let you check whether your impact theory is sound and adjust when it isn’t.

By thinking of your theory of change as a graph with nodes associated with different metrics, you can help make explicit between the metrics you can measure and control and the lagging output metrics that you care about such as revenue or usage. This can help justify the choice of a particular set of KPIs. It can help justify the certain changes when those key nodes in the graph are associated with controllable metrics. On the flip side, having a clear casual graph associated with your metrics can keep your use of metrics rigorous. 

### Tool (myfiles_browser) - 2025-01-19 16:32:06

*[tether_browsing_display content]*

### Tool (myfiles_browser) - 2025-01-19 16:32:06

All the files uploaded by the user have been fully loaded. Searching won't provide additional information.

### Assistant - 2025-01-19 16:32:06

Here’s a refined and more FLUX-aligned version of your draft, maintaining its core ideas while adding depth and richness:

---

**This Week’s Lens: The Causal Graph**

Amazon’s approach to leading indicators, famously centered on controllable input metrics, has reshaped how organizations think about operational focus. In *Platform Engineering*, authors Camille Fournier and Ian Nowland expand on this idea by grounding it in the framework of a causal graph:

> “Imagine constructing a causal graph, where nodes represent different inputs you might measure—like storage capacity or experiment throughput—and outputs that connect to other nodes. Each output varies in sensitivity to its inputs: for example, the number of experiments you can run might rise with throughput until hitting diminishing returns due to some limiting factor. Ultimately, the graph should converge on a KPI that drives business value, such as revenue.”

> “You should collect impact metrics at the interesting nodes in that graph… Metrics let you validate your impact theory and pivot when it doesn’t hold.”

By conceptualizing your theory of change as a network of cause-and-effect relationships, where nodes are tied to measurable metrics, you create a map linking the controllable and the consequential. This lens illuminates the pathways between inputs (what you can influence) and outputs (what you aim to achieve). It strengthens your ability to choose KPIs with intention, ensuring they reflect the underlying dynamics of your system.

A well-crafted causal graph also acts as a guardrail for metric design. By surfacing the connections and sensitivities between nodes, it helps maintain discipline and rigor. It prevents "metric myopia" by forcing you to trace a metric’s relevance back to core business outcomes, while simultaneously encouraging you to experiment and adapt when reality deviates from the model.

This lens not only sharpens strategic clarity but also democratizes it. When teams understand their metrics’ position in the causal graph, they gain agency to innovate within boundaries aligned to larger goals. It’s a way of thinking that’s both systemic and actionable, helping organizations thrive in the complex interplay between inputs, processes, and outcomes.

