# JS Essentials in making API

_Async function_
binding for new async function,
Replacing promice chain and improving code syntax

    Core feature and work
    > Making readable promise based behavior

    [[ Promise chain : .then() chaining of async operations]]
    Async working principle in JS:

        A mechanism for making smooth working promise based chain for the application and alowing other code to run

        Doesnt it makes same time requirements and how much different would it be if it was really implemented into other physical cpu core ?
            ~ Without real mutlitasking JS engine calls webapi for making the calls for Fetch api and get the information.
            ~ Await makes bookmark for promise to come back later.

# FETCH :)

## Fetch API internals

Power of fetch API calls,
Designed as complte interface for restfull api + Idempotent -> Multiple delte request = one request

## Fetch API calling behaviour

- Promise returned doesnt reject for HTTP code status for 400
  Promise resolves with
  Internal Server Error
  Bad request or not found given by server

        Must check with response.ok to see if its under 200-299 range

  Promise rejection range
  Network failior , DNS issue, CORS voilation which blocks request entirely

  credentials option is for handeling browser cookies omit for saving from not sending crendentials in requests

** Simple Promise based mechanism for handle resolve and rejection code for the given process **
Function -> rejects ~ resolution | resolves ~ resolutionS

$$ Fetch Information Internals working $$
High level wrapper for the Promise object

Workflow comparision with Promise based and its wrapper fetch based
fetch unifies the error handle stream for easy error handle with promise object simplification of complex promise chaining

    **Must Do experiment with managing the complexity with promise into replicating the behaviour of the given concept**

---

_SFC_
Single file component
A way of making components in single file including logic, js and template with file format .vue

## Fundamental Problem of trust and reliability with non-blocking execution

> Making Easy Data flow for multi execution flow in application> Easy Error handle for data flow clashes across two ends
> Makes sure app runs with promise under the hood

# VUE Life cycle hooks

Stages of vue component and its hooks

1. Creation | component initialized but DOM isnt ready | beforeCreate, created
2. Mounting | DOM inserted component , dom manupulation ideal or data fetching requests || beforeMount, mounted
3. Updating | reactive data changes -> Trigger data rerender
4. Unmounted | component is being removed | beforeUnmount, unmounted

Q : Why Lifecycle hooks are not Async
Its strictly made with being syncronous loading + Impacts component render due to usual component strict requirements + Loading Data prior to execution for straight loading is required for handeling component life cycle smooth execution

## Information fetching detail with lifehooks

Lifecycle hooks cant be synchronous but we require to fetch information to display with component
solution : using async function call inside hoocks for making the call for the information and presenting it into mounted component

## Forced Rest implementation in making API

> Performance bottleneck [ How ?]
> Non requried complexity of code
> functionality gaps in mordern ways

Critical Issue
Client needs user name -> we fetching entire json for whole client information wasting bandwidth
Increased latency for single information we client might require to fetch multiple api sources increasing latency
Alternative GraphQL lets user be specific for fetching information

    Rest api cant be  used for implenting realtime data passing for the critical applications like chat rooms due to latency thus websockets are used for the realtime connection

    rest api is best for simple structured way but i need to explore other ways for making more reliable endpoints
