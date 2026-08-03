// Hand-maintained product-scope boundary for the Galaxy Evolution Lab.
//
// The generated frontier data intentionally stays broad (astro-ph.GA + CO) so the
// evidence corpus is not narrowed. Product ranking and study selection must apply
// this stricter scientific boundary instead of treating every GA-dominant cluster
// as Galaxy Evolution. Unknown future clusters fail closed until reviewed.

export type FrontierScope = "core" | "adjacent" | "out_of_scope";

export const GALAXY_EVOLUTION_SCOPE_DEFINITION: Readonly<Record<FrontierScope, string>> = {
  core: "Directly studies how galaxies form, assemble, enrich, regulate gas and star formation, quench, or co-evolve with central black holes across cosmic time.",
  adjacent: "Provides supporting probes, environments, fossil records, or methods, but does not itself center galaxy evolution.",
  out_of_scope: "Centers stellar, transient, cosmological, gravitational, or particle physics rather than galaxy evolution.",
};

export const GALAXY_EVOLUTION_SCOPE_IDS = {
  core: [17, 19, 27, 35, 40, 41, 46, 56],
  adjacent: [0, 1, 2, 4, 5, 7, 8, 10, 15, 16, 18, 21, 22, 25, 28, 29, 31, 32, 45, 48, 50, 51, 52, 53, 54, 55],
  out_of_scope: [3, 6, 9, 11, 12, 13, 14, 20, 23, 24, 26, 30, 33, 34, 36, 37, 38, 39, 42, 43, 44, 47, 49],
} as const satisfies Readonly<Record<FrontierScope, readonly number[]>>;

const SCOPE_ORDER: readonly FrontierScope[] = ["core", "adjacent", "out_of_scope"];

export function galaxyEvolutionScope(cluster: number): FrontierScope {
  for (const classification of SCOPE_ORDER) {
    if ((GALAXY_EVOLUTION_SCOPE_IDS[classification] as readonly number[]).includes(cluster)) {
      return classification;
    }
  }
  return "out_of_scope";
}

export function isCoreGalaxyEvolutionFrontier(cluster: number): boolean {
  return galaxyEvolutionScope(cluster) === "core";
}

export function coreGalaxyEvolutionFrontiers<T extends { cluster: number; scoreV1: number }>(
  frontiers: readonly T[],
): T[] {
  return frontiers
    .filter((frontier) => frontier.scoreV1 > 0 && isCoreGalaxyEvolutionFrontier(frontier.cluster))
    .sort((a, b) => b.scoreV1 - a.scoreV1 || a.cluster - b.cluster);
}
