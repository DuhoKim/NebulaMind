import QAClient from "./QAClient";

async function getQuestions() {
  try {
    const res = await fetch("http://localhost:8000/api/qa", {
      next: { revalidate: 60 },
    });
    return res.ok ? res.json() : [];
  } catch {
    return [];
  }
}

async function getPages() {
  try {
    const res = await fetch("http://localhost:8000/api/pages", {
      next: { revalidate: 3600 },
    });
    return res.ok ? res.json() : [];
  } catch {
    return [];
  }
}

export default async function QAPage() {
  const [questions, pages] = await Promise.all([getQuestions(), getPages()]);
  return <QAClient initialQuestions={questions} initialPages={pages} />;
}
