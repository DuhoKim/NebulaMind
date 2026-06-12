import React from 'react';
import { render, screen } from '@testing-library/react';
import ClaimBlock from './ClaimBlock';

const mockClaim = {
  id: 1,
  text: 'Test Claim',
  trust_level: 'consensus',
  evidence_count: 1,
  section: 'Test Section',
};

const mockEvidence = {
  id: 1,
  title: 'Test Evidence',
  arxiv_id: '1234.5678',
  url: 'https://arxiv.org/abs/1234.5678',
  authors: 'Test Author',
  year: 2023,
  summary: 'This is a test summary.',
  stance: 'supports',
  votes_agree: 1,
  votes_disagree: 0,
  comments_count: 0,
  element_links: [
    {
      element_id: 'test-element-1',
      element_text_snapshot: 'This is a test element.',
    },
  ],
  link_count: 1,
};

describe('ClaimBlock', () => {
  it('renders the element link badge when element_links are present', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        json: () => Promise.resolve({ evidence: [mockEvidence], total_elements: 1 }),
      })
    ) as jest.Mock;

    render(<ClaimBlock claim={mockClaim} showColors={true} />);

    const evidenceButton = screen.getByTitle('🟢 Consensus · 1 source(s)');
    evidenceButton.click();

    const badge = await screen.findByText('supports: element 1 of 1');
    expect(badge).toBeInTheDocument();
  });
});
