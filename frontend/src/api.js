const API = import.meta.env.VITE_API_URL || '/api'

export async function request(path, options = {}) {
  const token = localStorage.getItem('tsms_token')
  const response = await fetch(`${API}${path}`, {
    ...options,
    headers: {
      ...(options.body ? { 'Content-Type': 'application/json' } : {}),
      ...(token ? { Authorization: `Token ${token}` } : {}),
      ...options.headers,
    },
  })
  if (response.status === 204) return null
  const data = await response.json().catch(() => ({}))
  if (!response.ok) throw new Error(data.detail || Object.values(data).flat().join(' ') || 'The request could not be completed.')
  return data
}

export const api = {
  login: (username, password) => request('/auth/login/', { method: 'POST', body: JSON.stringify({ username, password }) }),
  me: () => request('/auth/me/'),
  logout: () => request('/auth/logout/', { method: 'POST' }),
  categories: () => request('/categories/'),
  supportUsers: () => request('/users/support/'),
  tickets: (params = '') => request(`/tickets/${params}`),
  ticket: (id) => request(`/tickets/${id}/`),
  createTicket: (body) => request('/tickets/', { method: 'POST', body: JSON.stringify(body) }),
  assign: (id, assigneeName) => request(`/tickets/${id}/assign/`, { method: 'POST', body: JSON.stringify({ assignee_name: assigneeName }) }),
  workflow: (id, body) => request(`/tickets/${id}/update_workflow/`, { method: 'POST', body: JSON.stringify(body) }),
  priority: (id, body) => request(`/tickets/${id}/override_priority/`, { method: 'POST', body: JSON.stringify(body) }),
  note: (id, body) => request(`/tickets/${id}/notes/`, { method: 'POST', body: JSON.stringify(body) }),
  escalate: (id, body) => request(`/tickets/${id}/escalate/`, { method: 'POST', body: JSON.stringify(body) }),
  reopen: (id, reason) => request(`/tickets/${id}/request_reopening/`, { method: 'POST', body: JSON.stringify({ reason }) }),
  notifications: () => request('/notifications/'),
  report: () => request('/reports/summary/'),
}
