# Index for topics
Important topics with the vue instances and component flow

## Vue Criticals
+ State management

    Sharing a peice of information to multiple instances inside a application
    use reactive() ~ Making reactive objects and import to other components
    Making single source of truth for both of the elementsk
    
    ** If global storage could be edited by any of the components then it would make chaos for mentaining those variabels 

    Solution : Use central editing tool with the component for mentanning the central state for the given variable


+ MVC and state view action protocol for VUE
   Action protocol and event management in vue
   Normally no Buble for the given vue events takes place, 
    Events emited doesnt buble up, startight to the required element only.
    
+ Parent Child data flow mechanism
child emits the actions for the  state change request to the parent parent listens to the event and makes the changes and validation of emits for the child for final action and proces
    $emit()
    A important way for elements communication with forwarding information form child to parents via listeners in parent to listen 

    if event is click -> parent wont listen to native click
    Bloking usual behaviour for the childs emits

## Routing
Navigating website with unique location inside the given resources 
Ways for makng routing
    + File based routing
        Simple All files have their routes
    + Dynamic routing
        Making route for differnet information based
    + API routes
        Serving endpoint in the server
    + Data Fetching methods
        Simple data fetching requesting functions from api calls
+ Page composition
    
+ Dynamic routing
+ Router need
+ UX touch
+ SPA
+ Web workers

## Composition API
makig vue components using imported function instead of declaring options
    * Reactivity API
    * Lifecucle Hooks
        Making progrmatically hocking into lifecycle of component
    * Dependency injection
        reactivity api with injections
        What these stuff do realy ?


