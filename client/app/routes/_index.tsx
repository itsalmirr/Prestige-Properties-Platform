import type { MetaFunction } from '@remix-run/node'

export const meta: MetaFunction = () => {
  return [
    { title: 'New Remix App' },
    { name: 'description', content: 'Welcome to Remix!' },
  ]
}

const Index = () => {
  return (
    <div>
      <h1>Hello!</h1>
    </div>
  )
}

export default Index
