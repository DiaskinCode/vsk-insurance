<template>
  <div class="app-input-group d-f">
    <slot ></slot>
  </div>
</template>

<script>
export default {
  name: 'AppInputGroup',
  props: {},
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
.app-input-group {
  & > .p-component,
  & > .p-inputwrapper > .p-inputtext,
  & > .p-float-label > .p-component {
    border-radius: 0;
    margin: 0;
  }
  & > .p-component:focus,
  & > .p-inputwrapper > .p-inputtext:focus,
  & > .p-float-label > .p-component:focus {
    z-index: 1;
  }
  & > .p-component:focus ~ label,
  & > .p-inputwrapper > .p-inputtext:focus ~ label,
  & > .p-float-label > .p-component:focus ~ label {
    z-index: 1;
  }

  &-addon:first-child,
  & button:first-child,
  & input:first-child,
  & > .p-inputwrapper:first-child,
  & > .p-inputwrapper:first-child > .p-inputtext {
    border-top-left-radius: 1.5rem;
    border-bottom-left-radius: 1.5rem;
  }

  & .p-float-label:first-child input {
    border-top-left-radius: 1.5rem;
    border-bottom-left-radius: 1.5rem;
  }

  &-addon:last-child,
  & button:last-child,
  & input:last-child,
  & > .p-inputwrapper:last-child,
  & > .p-inputwrapper:last-child > .p-inputtext {
    border-top-right-radius: 1.5rem;
    border-bottom-right-radius: 1.5rem;
  }

  & .p-float-label:last-child input {
    border-top-right-radius: 1.5rem;
    border-bottom-right-radius: 1.5rem;
  }
}
</style>
