import { notFound } from "next/navigation";
import AgentProfileClient from "./AgentProfileClient";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

type Props = { params: Promise<{ id: string }> };

async function agentExists(id: string): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE}/api/agents/${id}/profile`, { next: { revalidate: 3600 } });
    return res.ok;
  } catch {
    return false;
  }
}

export default async function AgentProfilePage({ params }: Props) {
  const { id } = await params;
  if (!(await agentExists(id))) notFound();
  return <AgentProfileClient />;
}
