<template>
  <MultiSelect
    class="app-multi-select"
    :show-toggle-all="showToggleAll"
    :display="display"
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
  </MultiSelect>
</template>

<script>
export default {
  name: 'AppMultiSelect',
  props: {
    showToggleAll: {
      type: Boolean,
      default: false,
    },
    display: {
      type: String,
      default: 'chip',
    },
  },
  data: () => ({
  }),
  computed: {
  },
  methods: {
  },
};
</script>

<style lang="scss">
#__nuxt .app-multi-select {
  .p-multiselect-item {
    white-space: normal;
    font-size: 1.4rem;
    display: flex;
    align-items: center;
  }
  .p-multiselect-label {
    height: 100%;
    display: flex;
    align-items: center;
    padding: 1.5rem 2rem;
    font-size: 1.6rem;
  }
  &.p-inputwrapper-filled .p-multiselect-label {
    padding: 0.8rem 2rem;
  }
  .p-multiselect-filter-container {
    display: flex;
    align-items: center;
  }
  .p-multiselect-filter {
    padding-top: 1rem;
    padding-bottom: 1rem;
    padding-left: 1.25rem;
    padding-right: 3.25rem;
    border-radius: .5rem;
    font-size: 1.6rem;
  }
  .p-multiselect-panel {
    overflow: hidden;
    max-height: 30rem !important;
    @media (max-width: 600px) {
      max-height: 30vh !important;
    }
  }
  .p-multiselect-filter-icon {
    font-size: 1.6rem;
    top: 1.7rem;
    right: 1.2rem;
  }
  .p-multiselect-empty-message {
    font-size: 1.6rem;
    text-align: center;
  }
  .p-multiselect-token {
    display: flex;
    align-items: center;
  }
  .p-multiselect-token-label {
    font-size: 1.3rem;
    display: flex;
    align-items: center;
    padding: .6rem .75rem;
  }
  .p-multiselect-token-icon {
    font-size: 1.3rem;
    margin-left: 0;
  }
  .p-multiselect-trigger {
    color: $primary;
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
    padding: 0 2.5rem;
  }
  .p-multiselect-trigger-icon {
    transition: transform .2s ease;
  }

  .p-checkbox {
    width: 2.4rem;
    height: 2.4rem;
    margin-right: 1rem;
    @media (max-width: 600px) {
      width: 3rem;
      height: 3rem;
    }
  }
  .p-checkbox .p-checkbox-box {
    border: 2px solid #ced4da;
    background: #ffffff;
    width: 2.4rem;
    height: 2.4rem;
    color: #495057;
    border-radius: 1rem;
    transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
    @media (max-width: 600px) {
      width: 3rem;
      height: 3rem;
      border-radius: 1.2rem;
    }
  }
  .p-checkbox .p-checkbox-box .p-checkbox-icon {
    transition-duration: 0.2s;
    color: #ffffff;
    font-size: 1.6rem;
    @media (max-width: 600px) {
      font-size: 1.8rem;
    }
  }
  .p-checkbox .p-checkbox-box.p-highlight {
    border-color: $primary;
    background: $primary;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box:hover {
    border-color: #2196F3;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box.p-focus {
    outline: 0 none;
    outline-offset: 0;
    box-shadow: 0 0 0 0.2rem #a6d5fa;
    border-color: #2196F3;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box.p-highlight:hover {
    border-color: $primary;
    background: $primary;
    color: #ffffff;
  }
  .p-checkbox.p-invalid > .p-checkbox-box {
    border-color: #f44336;
  }
}
</style>

<style lang="scss">
.p-multiselect {
  background: $white;
  border: .1rem solid $white;
  transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
  border-radius: 1.5rem;
  box-shadow: $box-shadow-1;
}
.p-multiselect:not(.p-disabled):hover {
  border-color: $primary;
}
.p-multiselect:not(.p-disabled).p-focus {
  outline: 0 none;
  outline-offset: 0;
  border-color: $primary;
}
.p-multiselect .p-multiselect-label {
  padding: 1.5rem 2rem;
  transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
}
.p-multiselect .p-multiselect-label.p-placeholder {
  color: #6c757d;
  @media (max-width: 600px) {
    font-size: 1.6rem;
  }
}
.p-multiselect.p-multiselect-chip .p-multiselect-token {
  padding: 0.25rem 0.5rem;
  margin-right: 0.5rem;
  background: #dee2e6;
  color: #495057;
  border-radius: 16px;
}
.p-multiselect.p-multiselect-chip .p-multiselect-token .p-multiselect-token-icon {
  margin-left: 0.5rem;
}
.p-multiselect .p-multiselect-trigger {
  background: transparent;
  color: #6c757d;
  width: 2.357rem;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px;
}
.p-multiselect.p-invalid.p-component {
  border-color: #f44336;
}

.p-inputwrapper-filled.p-multiselect.p-multiselect-chip .p-multiselect-label {
  padding: 0.25rem 0.5rem;
}

.p-multiselect-panel {
  background: #ffffff;
  color: #495057;
  border: 0 none;
  border-radius: 3px;
  box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 1px 10px 0 rgba(0, 0, 0, 0.12);
}
.p-multiselect-panel .p-multiselect-header {
  padding: 0.5rem 1rem;
  border-bottom: 0 none;
  color: #495057;
  background: #f8f9fa;
  margin: 0;
  border-top-right-radius: 3px;
  border-top-left-radius: 3px;
}
.p-multiselect-panel .p-multiselect-header .p-multiselect-filter-container .p-inputtext {
  padding-right: 1.5rem;
}
.p-multiselect-panel .p-multiselect-header .p-multiselect-filter-container .p-multiselect-filter-icon {
  right: 0.5rem;
  color: #6c757d;
}
.p-multiselect-panel .p-multiselect-header .p-checkbox {
  margin-right: 0.5rem;
}
.p-multiselect-panel .p-multiselect-header .p-multiselect-close {
  margin-left: 0.5rem;
  width: 2rem;
  height: 2rem;
  color: #6c757d;
  border: 0 none;
  background: transparent;
  border-radius: 50%;
  transition: background-color 0.2s, color 0.2s, box-shadow 0.2s;
}
.p-multiselect-panel .p-multiselect-header .p-multiselect-close:enabled:hover {
  color: #495057;
  border-color: transparent;
  background: #e9ecef;
}
.p-multiselect-panel .p-multiselect-header .p-multiselect-close:focus {
  outline: 0 none;
  outline-offset: 0;
  box-shadow: 0 0 0 0.2rem #a6d5fa;
}
.p-multiselect-panel .p-multiselect-items {
  padding: 0.5rem 0;
}
.p-multiselect-panel .p-multiselect-items .p-multiselect-item {
  margin: 0;
  padding: 0.5rem 1rem;
  border: 0 none;
  color: #495057;
  background: transparent;
  transition: box-shadow 0.2s;
  border-radius: 0;
}
.p-multiselect-panel .p-multiselect-items .p-multiselect-item.p-highlight {
  color: #495057;
  background: #E3F2FD;
}
.p-multiselect-panel .p-multiselect-items .p-multiselect-item:not(.p-highlight):not(.p-disabled):hover {
  color: #495057;
  background: #e9ecef;
}
.p-multiselect-panel .p-multiselect-items .p-multiselect-item:focus {
  outline: 0 none;
  outline-offset: 0;
  box-shadow: inset 0 0 0 0.15rem #a6d5fa;
}
.p-multiselect-panel .p-multiselect-items .p-multiselect-item .p-checkbox {
  margin-right: 0.5rem;
}
.p-multiselect-panel .p-multiselect-items .p-multiselect-item-group {
  margin: 0;
  padding: 0.75rem 1rem;
  color: #495057;
  background: #ffffff;
  font-weight: 600;
}
.p-multiselect-panel .p-multiselect-items .p-multiselect-empty-message {
  padding: 0.5rem 1rem;
  color: #495057;
  background: transparent;
}
.p-multiselect-panel .p-multiselect-items .p-multiselect-item .p-checkbox {
  margin-right: 0.5rem;
}

.app-multi-select {
  .p-checkbox {
    width: 20px;
    height: 20px;
  }
  .p-checkbox .p-checkbox-box {
    border: 2px solid #ced4da;
    background: #ffffff;
    width: 20px;
    height: 20px;
    color: #495057;
    border-radius: 3px;
    transition: background-color 0.2s, color 0.2s, border-color 0.2s, box-shadow 0.2s;
  }
  .p-checkbox .p-checkbox-box .p-checkbox-icon {
    transition-duration: 0.2s;
    color: #ffffff;
    font-size: 14px;
  }
  .p-checkbox .p-checkbox-box.p-highlight {
    border-color: #2196F3;
    background: #2196F3;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box:hover {
    border-color: #2196F3;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box.p-focus {
    outline: 0 none;
    outline-offset: 0;
    box-shadow: 0 0 0 0.2rem #a6d5fa;
    border-color: #2196F3;
  }
  .p-checkbox:not(.p-checkbox-disabled) .p-checkbox-box.p-highlight:hover {
    border-color: #0b7ad1;
    background: #0b7ad1;
    color: #ffffff;
  }
  .p-checkbox.p-invalid > .p-checkbox-box {
    border-color: #f44336;
  }
}
</style>
