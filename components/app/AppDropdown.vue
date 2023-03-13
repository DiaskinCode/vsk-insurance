<template>
  <Dropdown
    class="app-dropdown"
    :value="value"
    :options="options"
    :optionLabel="optionLabel"
    :optionValue="optionValue"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <template
      v-for="(_, slot) of $scopedSlots"
      v-slot:[slot]="scope"
    >
      <slot
        :name="slot"
        v-bind="scope"
      />
    </template>
  </Dropdown>
</template>

<script>
export default {
  name: 'AppDropdown',
  props: {
    value: {
      type: [String, Number],
      default: null,
    },
    options: {
      type: Array,
      default: () => [],
    },
    optionLabel: {
      type: [String, Function],
      default: '',
    },
    optionValue: {
      type: [String, Function],
      default: '',
    },
  },
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
#__nuxt .app-dropdown {
  .p-dropdown-item {
    white-space: normal;
    font-size: 1.4rem;
  }
  .p-dropdown-filter-container {
    display: flex;
    align-items: center;
  }
  .p-dropdown-filter {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1.25rem;
    padding-right: 3.25rem;
    border-radius: .5rem;
    font-size: 1.6rem;
  }
  .p-dropdown-items-wrapper {
    max-height: 30rem !important;
    @media (max-width: 600px) {
      max-height: 24vh !important;
    }
  }
  .p-dropdown-filter-icon {
    font-size: 1.6rem;
    top: 1.7rem;
    right: 1.2rem;
  }
  .p-dropdown-empty-message {
    font-size: 1.6rem;
    text-align: center;
  }
}

.app-dropdown {
  &.p-dropdown {
    background: $white;
    border: .1rem solid $white;
    transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
    border-radius: 1.5rem;
    box-shadow: $box-shadow-1;
  }
  &.p-dropdown:not(.p-disabled):hover {
    border-color: $primary;
  }
  &.p-dropdown:not(.p-disabled).p-focus {
    outline: 0 none;
    outline-offset: 0;
    border-color: $primary;
  }
  &.p-dropdown.p-dropdown-clearable .p-dropdown-label {
    padding-right: 1.5rem;
  }
  &.p-dropdown .p-dropdown-label {
    background: transparent;
    padding: 1.5rem 2rem;
    border: 0 none;
    @media (max-width: 600px) {
      font-size: 1.6rem;
    }
  }
  &.p-dropdown .p-dropdown-label.p-placeholder {
    color: #6c757d;
    @media (max-width: 600px) {
      font-size: 1.6rem;
    }
  }
  &.p-dropdown .p-dropdown-label:enabled:focus {
    outline: 0 none;
    box-shadow: none;
  }
  &.p-dropdown .p-dropdown-trigger {
    background: transparent;
    color: $primary;
    width: 2.357rem;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    margin-right: 2rem;
    .p-dropdown-trigger-icon {
      transition: transform .2s ease;
    }
    &[aria-expanded="true"] .p-dropdown-trigger-icon {
      transform: rotate(90deg);
    }
  }

  .p-dropdown-panel {
    background: #ffffff;
    color: #495057;
    border: 0 none;
    border-radius: 3px;
    box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 1px 10px 0 rgba(0, 0, 0, 0.12);
  }
  .p-dropdown-panel .p-dropdown-header {
    padding: 0.5rem 1rem;
    border-bottom: 0 none;
    color: #495057;
    background: #f8f9fa;
    margin: 0;
    border-top-right-radius: 3px;
    border-top-left-radius: 3px;
  }
  .p-dropdown-panel .p-dropdown-header .p-dropdown-filter {
    padding-right: 1.5rem;
    margin-right: -1.5rem;
  }
  .p-dropdown-panel .p-dropdown-header .p-dropdown-filter-icon {
    right: 0.5rem;
    color: #6c757d;
  }
  .p-dropdown-panel .p-dropdown-items {
    padding: 0.5rem 0;
  }
  .p-dropdown-panel .p-dropdown-items .p-dropdown-item {
    margin: 0;
    padding: 1rem 2rem;
    border: 0 none;
    color: #495057;
    background: transparent;
    transition: box-shadow 0.2s;
    border-radius: 0;
    @media (max-width: 600px) {
      font-size: 1.6rem;
    }
  }
  .p-dropdown-panel .p-dropdown-items .p-dropdown-item.p-highlight {
    color: #495057;
    background: #E3F2FD;
  }
  .p-dropdown-panel .p-dropdown-items .p-dropdown-item:not(.p-highlight):not(.p-disabled):hover {
    color: #495057;
    background: #e9ecef;
  }
  .p-dropdown-panel .p-dropdown-items .p-dropdown-item-group {
    margin: 0;
    padding: 0.75rem 1rem;
    color: #495057;
    background: #ffffff;
    font-weight: 600;
  }
  .p-dropdown-panel .p-dropdown-items .p-dropdown-empty-message {
    padding: 0.5rem 1rem;
    color: #495057;
    background: transparent;
  }
}
</style>
