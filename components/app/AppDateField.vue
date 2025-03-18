<template>
  <div class="app-date-field">
    <label class="label">Дата начала действия договора</label>
    <div class="input-wrapper">
      <input
        v-model="formattedDate"
        v-mask="'##.##.####'"
        type="text"
        class="app-input"
        placeholder="ДД.ММ.ГГГГ"
        @input="handleInput"
        @blur="validateDate"
      >
      <button type="button" class="calendar-button" @click="openDatePicker">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="gray"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="icon"
        >
          <rect
            x="3"
            y="4"
            width="18"
            height="16"
            rx="2"
            ry="2"
          />
          <line x1="16" y1="2" x2="16" y2="6" />
          <line x1="8" y1="2" x2="8" y2="6" />
          <line x1="3" y1="10" x2="21" y2="10" />
        </svg>
      </button>
    </div>
    <input ref="datePicker" type="date" class="hidden-date-picker" @input="handleDateSelect">
    <p v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </p>
  </div>
</template>

<script>
import { mask } from 'vue-the-mask';

export default {
  name: 'AppDateField',
  directives: { mask },
  props: {
    value: { type: String, default: '' },
    isWithoutSport: { type: Boolean, default: false }, // Флаг "Без спорта"
  },
  data() {
    return {
      formattedDate: this.value || '',
      errorMessage: '',
    };
  },
  watch: {
    value(newValue) {
      this.formattedDate = newValue;
    },
  },
  methods: {
    openDatePicker() {
      this.$refs.datePicker.showPicker();
    },
    handleDateSelect(event) {
      const date = new Date(event.target.value);
      if (!isNaN(date.getTime())) {
        this.formattedDate = date.toLocaleDateString('ru-RU');
        this.validateDate();
        this.$emit('input', this.formattedDate);
      }
    },
    handleInput() {
      this.$emit('input', this.formattedDate);
    },
    validateDate() {
      if (!this.formattedDate) {
        this.errorMessage = 'Обязательное поле';
        return;
      }

      const [day, month, year] = this.formattedDate.split('.').map(Number);
      const selectedDate = new Date(year, month - 1, day);
      const today = new Date();
      today.setHours(0, 0, 0, 0);

      const minDate = new Date(today);
      minDate.setDate(minDate.getDate() + 1); // +1 день от текущей даты (общая логика)

      const maxDate = new Date(today);
      if (this.isWithoutSport) {
        maxDate.setDate(maxDate.getDate() + 90); // Для "без спорта" +90 дней
      } else {
        maxDate.setFullYear(today.getFullYear() + 1); // Для всех остальных +1 год
      }

      if (selectedDate < minDate) {
        this.errorMessage = 'Дата должна быть не ранее чем через 1 день от даты оформления';
        return;
      }

      if (selectedDate > maxDate) {
        this.errorMessage = this.isWithoutSport
          ? 'Дата не должна быть более чем на 90 дней от даты оформления'
          : 'Дата не должна превышать 1 год от даты оформления';
        return;
      }

      this.errorMessage = '';
    },
  },
};
</script>

  <style lang="scss">
  .app-date-field {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: start;
    max-width: 400px;
    width: 100%;
  }
  .label {
    font-size: 14px;
    margin-bottom: 4px;
    color: #333;
  }
  .input-wrapper {
    display: flex;
    align-items: center;
    width: 100%;
    position: relative;
  }
  .app-input {
    flex: 1;
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 16px;
  }
  .calendar-button {
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
  }
  .icon {
    width: 24px;
    height: 24px;
  }
  .hidden-date-picker {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
  }
  .error-message {
    color: red;
    font-size: 14px;
    margin-top: 4px;
  }
  </style>
